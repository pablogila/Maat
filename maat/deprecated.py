from .core import *


def plot_ins(ins:INS):
    fig, ax = plt.subplots()

    # Limit max intensity to INS.ylim_scale times the MAPI peak of the 1st dataframe
    df0 = ins.dataframes[0]

    if ins.scale_range and len(ins.scale_range) == 2:
        range_start = ins.scale_range[0]
        range_end = ins.scale_range[1]
    else:
        range_start = 30
        range_end = 50

    df_range = df0[(df0[df0.columns[0]] >= range_start) & (df0[df0.columns[0]] <= range_end)]
    max_df = df_range[df_range.columns[1]].max()

    ax.set_xlim([0, ins.xlim])
    ax.set_ylim([0, ins.ylim_scale * max_df])

    strings_to_delete_from_name = ['.csv', '_INS', '_temp', '_cellsubtracted']
    for df, name in zip(ins.dataframes, ins.filenames):
        if ins.scale_range is not False:
            first_cut = ins.scale_range[0]
            second_cut = ins.scale_range[1]
            df_range_i = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            max_df_i = df_range_i[df_range_i.columns[1]].max()
            df[df.columns[1]] = df[df.columns[1]] / max_df_i * max_df
        name_clean = name
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

        if ins.baseline is not None and ins.baseline_error is not None:
            ax.fill_between(df[df.columns[0]], ins.baseline - ins.baseline_error, ins.baseline + ins.baseline_error, color='gray', alpha=0.5, label='Peak baseline')
        elif ins.baseline is not None:
            ax.axhline(y=ins.baseline, color='black', linestyle='--', label='Peak baseline')


    plt.title(ins.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if ins.log:
        ax.set_xscale_range('log')
    if ins.hide_y_axis:
        ax.set_yticks([])
    if ins.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    root = os.getcwd()
    save_name = os.path.join(root, ins.save_as)
    # plt.savefig(save_name)
    plt.show()


def plot_atr(atr:ATR):
    
    if atr.figsize:
        fig, ax = plt.subplots(figsize=atr.figsize)
    else:
        fig, ax = plt.subplots()

    if atr.x_low_lim:
        ax.set_xlim(left=atr.x_low_lim)
    if atr.x_top_lim:
        ax.set_xlim(right=atr.x_top_lim)
    if atr.y_low_lim:
        ax.set_ylim(bottom=atr.y_low_lim)
    if atr.y_top_lim:
        ax.set_ylim(top=atr.y_top_lim)

    if atr.scale_range:
        df0 = atr.dataframes[0]
        df0 = df0[(df0[df0.columns[0]] >= atr.scale_range[0]) & (df0[df0.columns[0]] <= atr.scale_range[1])]
        max_df = df0[df0.columns[1]].max()
        ax.set_ylim(top=atr.scale_y*max_df)

    strings_to_delete_from_name = ['.csv', '_INS', '_temp']
    for df, name in zip(atr.dataframes, atr.filenames):
        if atr.scale_range:
            first_cut = atr.scale_range[0]
            second_cut = atr.scale_range[1]
            df_range_i = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            max_df_i = df_range_i[df_range_i.columns[1]].max()
            df[df.columns[1]] = max_df * (df[df.columns[1]] / max_df_i)
        
        if (atr.y_offset is True) and (atr.y_low_lim is not None) and (atr.y_top_lim is not None):
            number_of_plots = len(atr.dataframes)
            height = atr.y_top_lim - atr.y_low_lim
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (atr.filenames.index(name) * height) / number_of_plots

        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if atr.legend and isinstance(atr.legend, list):
            name_clean = atr.legend[atr.filenames.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    plt.title(atr.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if atr.log:
        ax.set_xscale('log')
    if atr.hide_y_axis:
        ax.set_yticks([])
    if atr.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if atr.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, atr.save_as)
        plt.savefig(save_name)
    
    plt.show()


def normalize(spectra:Spectra):
    '''Deprecated on vMT.0.1.0.'''
    sdata = deepcopy(spectra)
    if hasattr(sdata, 'scale_range') and sdata.scale_range is not None:
        scale_range = sdata.scale_range
    else:
        scale_range = ScaleRange(
            xmin=min(df0[df0.columns[0]]),
            xmax=max(df0[df0.columns[0]]),
            index=0,
        )
    df_index = scale_range.index if scale_range.index else 0
    df0 = sdata.dataframe[df_index]
    
    if scale_range.ymax:
        return _normalize_y(sdata)

    xmin = scale_range.xmin
    xmax = scale_range.xmax

    df0 = df0[(df0[df0.columns[0]] >= xmin) & (df0[df0.columns[0]] <= xmax)]
    ymax_on_range = df0[df0.columns[1]].max()
    normalized_dataframes = []
    for df in sdata.dataframe:
        df_range = df[(df[df.columns[0]] >= xmin) & (df[df.columns[0]] <= xmax)]
        i_ymax_on_range = df_range[df_range.columns[1]].max()
        df[df.columns[1]] =  df[df.columns[1]] * ymax_on_range / i_ymax_on_range
        normalized_dataframes.append(df)
    sdata.dataframe = normalized_dataframes
    return sdata


def peaks_mapi(ins:Spectra,
         peaks:dict,
         df_index:int=0,
         ):
    '''
    DEPRECATED after v1.0.3\n
    Calculate the deuteration of MAPI by integrating the INS disrotatory peaks.\n
    'peaks' must be a dictionary with the peak limits and the baseline.\n
    Peak keywords required for partial deuteration: h6d0, h5d1, h4d2, h3d3\n
    Additional peak keywords required for total deuteration: h2d4, h1d5, h0d6\n
    If some peak is not present, just set the limits to a small baseline plateau.\n
    Peaks example:\n
    peaks = {
        'baseline' : None,
        'baseline_error' : None,
        'h6d0' : [41, 43],
        'h5d1' : [41, 43],
        'h4d2' : [41, 43],
        'h3d3' : [34.7, 37.3],
        'h2d4' : [31.0, 33.0],
        'h1d5' : [28.0, 30.5],
        'h0d6' : [26.5, 28.0],
        }
    '''

    peak_data = deepcopy(ins)

    baseline = 0.0
    baseline_error = 0.0
    if 'baseline' in peaks:
        if peaks['baseline'] is not None:
            baseline = peaks['baseline']
    if 'baseline_error' in peaks:
        if peaks['baseline_error'] is not None:
            baseline_error = peaks['baseline_error']

    run_partial = True
    run_total = True

    h6d0_limits = None
    h5d1_limits = None
    h4d2_limits = None
    h3d3_limits = None
    h2d4_limits = None
    h1d5_limits = None
    h0d6_limits = None

    if 'h6d0' in peaks:
        h6d0_limits = peaks['h6d0']
    if 'h5d1' in peaks:
        h5d1_limits = peaks['h5d1']
    if 'h4d2' in peaks:
        h4d2_limits = peaks['h4d2']
    if 'h3d3' in peaks:
        h3d3_limits = peaks['h3d3']
    if 'h2d4' in peaks:
        h2d4_limits = peaks['h2d4']
    if 'h1d5' in peaks:
        h1d5_limits = peaks['h1d5']
    if 'h0d6' in peaks:
        h0d6_limits = peaks['h0d6']

    if h0d6_limits is None or h1d5_limits is None or h2d4_limits is None or h3d3_limits is None:
        run_total = False
    if h6d0_limits is None or h5d1_limits is None or h4d2_limits is None or h3d3_limits is None:
        run_partial = False

    if not run_partial:
        raise ValueError('No peaks to integrate. Remember to assign peak limits as a dictionary with the keys: h6d0, h5d1, h4d2, h3d3, h2d4, h1d5, h0d6.')

    h6d0_area, h6d0_area_error = area_under_peak(peak_data, [h6d0_limits[0], h6d0_limits[1], baseline, baseline_error], df_index)
    h5d1_area, h5d1_area_error = area_under_peak(peak_data, [h5d1_limits[0], h5d1_limits[1], baseline, baseline_error], df_index)
    h4d2_area, h4d2_area_error = area_under_peak(peak_data, [h4d2_limits[0], h4d2_limits[1], baseline, baseline_error], df_index)
    h3d3_area, h3d3_area_error = area_under_peak(peak_data, [h3d3_limits[0], h3d3_limits[1], baseline, baseline_error], df_index)
    h6d0_area /= 6
    h5d1_area /= 5
    h4d2_area /= 4
    h3d3_area /= 3
    
    if not run_total:
        total_area = h6d0_area + h5d1_area + h4d2_area + h3d3_area

        h6d0_ratio = h6d0_area / total_area
        h5d1_ratio = h5d1_area / total_area
        h4d2_ratio = h4d2_area / total_area
        h3d3_ratio = h3d3_area / total_area

        deuteration = 0 * h6d0_ratio + (1/3) * h5d1_ratio + (2/3) * h4d2_ratio + 1 * h3d3_ratio
        protonation = 1 * h6d0_ratio + (2/3) * h5d1_ratio + (1/3) * h4d2_ratio + 0 * h3d3_ratio

        # Error propagation

        total_area_error = np.sqrt(h6d0_area_error**2 + h5d1_area_error**2 + h4d2_area_error**2 + h3d3_area_error**2)

        h6d0_error = abs(h6d0_area) * np.sqrt((h6d0_area_error/h6d0_area)**2 + (total_area_error/total_area)**2)
        h5d1_error = abs(h5d1_area) * np.sqrt((h5d1_area_error/h5d1_area)**2 + (total_area_error/total_area)**2)
        h4d2_error = abs(h4d2_area) * np.sqrt((h4d2_area_error/h4d2_area)**2 + (total_area_error/total_area)**2)
        h3d3_error = abs(h3d3_area) * np.sqrt((h3d3_area_error/h3d3_area)**2 + (total_area_error/total_area)**2)

        deuteration_error = np.sqrt(h5d1_error**2 + h4d2_error**2 + h3d3_error**2)
        protonation_error = np.sqrt(h6d0_error**2 + h5d1_error**2 + h4d2_error**2)

    if run_total:
        h2d4_area, h2d4_area_error = area_under_peak(peak_data, [h2d4_limits[0], h2d4_limits[1], baseline, baseline_error], df_index)
        h1d5_area, h1d5_area_error = area_under_peak(peak_data, [h1d5_limits[0], h1d5_limits[1], baseline, baseline_error], df_index)
        h0d6_area, h0d6_area_error = area_under_peak(peak_data, [h0d6_limits[0], h0d6_limits[1], baseline, baseline_error], df_index)
        h2d4_area /= 2
        h1d5_area /= 1
        h0d6_area /= 1

        total_area_CDND = h6d0_area + h5d1_area + h4d2_area + h3d3_area + h2d4_area + h1d5_area + h0d6_area

        h6d0_ratio_CDND = h6d0_area / total_area_CDND
        h5d1_ratio_CDND = h5d1_area / total_area_CDND
        h4d2_ratio_CDND = h4d2_area / total_area_CDND
        h3d3_ratio_CDND = h3d3_area / total_area_CDND
        h2d4_ratio_CDND = h2d4_area / total_area_CDND
        h1d5_ratio_CDND = h1d5_area / total_area_CDND
        h0d6_ratio_CDND = h0d6_area / total_area_CDND

        deuteration_CDND = 0 * h6d0_ratio_CDND + (1/6) * h5d1_ratio_CDND + (2/6) * h4d2_ratio_CDND + (3/6) * h3d3_ratio_CDND + (4/6) * h2d4_ratio_CDND + (5/6) * h1d5_ratio_CDND + 1 * h0d6_ratio_CDND
        protonation_CDND = 1 * h6d0_ratio_CDND + (5/6) * h5d1_ratio_CDND + (4/6) * h4d2_ratio_CDND + (3/6) * h3d3_ratio_CDND + (2/6) * h2d4_ratio_CDND + (1/6) * h1d5_ratio_CDND + 0 * h0d6_ratio_CDND

        deuteration_CDND_amine = 0 * h3d3_ratio_CDND + (1/3) * h2d4_ratio_CDND + (2/3) * h1d5_ratio_CDND + 1 * h0d6_ratio_CDND
        protonation_CDND_amine = 1 * h3d3_ratio_CDND + (2/3) * h2d4_ratio_CDND + (1/3) * h1d5_ratio_CDND + 0 * h0d6_ratio_CDND

        # Error propagation

        total_area_error_CDND = np.sqrt(h6d0_area_error**2 + h5d1_area_error**2 + h4d2_area_error**2 + h3d3_area_error**2 + h2d4_area_error**2 + h1d5_area_error**2 + h0d6_area_error**2)

        h6d0_error_CDND = abs(h6d0_area) * np.sqrt((h6d0_area_error/h6d0_area)**2 + (total_area_error_CDND/total_area_CDND)**2)
        h5d1_error_CDND = abs(h5d1_area) * np.sqrt((h5d1_area_error/h5d1_area)**2 + (total_area_error_CDND/total_area_CDND)**2)
        h4d2_error_CDND = abs(h4d2_area) * np.sqrt((h4d2_area_error/h4d2_area)**2 + (total_area_error_CDND/total_area_CDND)**2)
        h3d3_error_CDND = abs(h3d3_area) * np.sqrt((h3d3_area_error/h3d3_area)**2 + (total_area_error_CDND/total_area_CDND)**2)
        h2d4_error_CDND = abs(h2d4_area) * np.sqrt((h2d4_area_error/h2d4_area)**2 + (total_area_error_CDND/total_area_CDND)**2)
        h1d5_error_CDND = abs(h1d5_area) * np.sqrt((h1d5_area_error/h1d5_area)**2 + (total_area_error_CDND/total_area_CDND)**2)
        h0d6_error_CDND = abs(h0d6_area) * np.sqrt((h0d6_area_error/h0d6_area)**2 + (total_area_error_CDND/total_area_CDND)**2)

        deuteration_CDND_error = np.sqrt(h5d1_error_CDND**2 + h4d2_error_CDND**2 + h3d3_error_CDND**2 + h2d4_error_CDND**2 + h1d5_error_CDND**2 + h0d6_error_CDND**2)
        protonation_CDND_error = np.sqrt(h0d6_error_CDND**2 + h1d5_error_CDND**2 + h2d4_error_CDND**2 + h3d3_error_CDND**2 + h4d2_error_CDND**2 + h5d1_error_CDND**2)

        deuteration_CDND_amine_error = np.sqrt(h2d4_error_CDND**2 + h1d5_error_CDND**2 + h0d6_error_CDND**2)
        protonation_CDND_amine_error = np.sqrt(h1d5_error_CDND**2 + h2d4_error_CDND**2 + h3d3_error_CDND**2)

    print()
    if hasattr(ins, "plotting") and ins.plotting.legend != None:
        print(f'Sample:  {ins.plotting.legend[df_index]}')
    else:
        print(f'Sample:  {ins.filename[df_index]}')
    print(f'Corrected baseline: {round(baseline,2)} +- {round(baseline_error,2)}')
    if not run_total:
        print(f"HHH {h6d0_limits}:  {round(h6d0_ratio,2)}  +-  {round(h6d0_error,2)}")
        print(f"DHH {h5d1_limits}:  {round(h5d1_ratio,2)}  +-  {round(h5d1_error,2)}")
        print(f"DDH {h4d2_limits}:  {round(h4d2_ratio,2)}  +-  {round(h4d2_error,2)}")
        print(f"DDD {h3d3_limits}:  {round(h3d3_ratio,2)}  +-  {round(h3d3_error,2)}")
        print(f"Amine deuteration:  {round(deuteration,2)}  +-  {round(deuteration_error,2)}")
        print(f"Amine protonation:  {round(protonation,2)}  +-  {round(protonation_error,2)}")
        print()
        return f"{deuteration:.2f} +- {deuteration_error:.2f}"
    else:
        print(f"HHH-HHH {h6d0_limits}:  {round(h6d0_ratio_CDND,2)}  +-  {round(h6d0_error_CDND,2)}")
        print(f"DHH-HHH {h5d1_limits}:  {round(h5d1_ratio_CDND,2)}  +-  {round(h5d1_error_CDND,2)}")
        print(f"DDH-HHH {h4d2_limits}:  {round(h4d2_ratio_CDND,2)}  +-  {round(h4d2_error_CDND,2)}")
        print(f"DDD-HHH {h3d3_limits}:  {round(h3d3_ratio_CDND,2)}  +-  {round(h3d3_error_CDND,2)}")
        print(f"DDD-DHH {h2d4_limits}:  {round(h2d4_ratio_CDND,2)}  +-  {round(h2d4_error_CDND,2)}")
        print(f"DDD-DDH {h1d5_limits}:  {round(h1d5_ratio_CDND,2)}  +-  {round(h1d5_error_CDND,2)}")
        print(f"DDD-DDD {h0d6_limits}:  {round(h0d6_ratio_CDND,2)}  +-  {round(h0d6_error_CDND,2)}")
        print(f"Total deuteration:  {round(deuteration_CDND,2)}  +-  {round(deuteration_CDND_error,2)}")
        print(f"Total protonation:  {round(protonation_CDND,2)}  +-  {round(protonation_CDND_error,2)}")
        print(f"Amine deuteration:  {round(deuteration_CDND_amine,2)}  +-  {round(deuteration_CDND_amine_error,2)}")
        print(f"Amine protonation:  {round(protonation_CDND_amine,2)}  +-  {round(protonation_CDND_amine_error,2)}")
        print()
        return f"{deuteration_CDND_amine:.2f} +- {deuteration_CDND_amine_error:.2f} / {deuteration_CDND:.2f} +- {deuteration_CDND_error:.2f}"


def plateau(spectra:Spectra, cuts:list, df_index:int=0):
    '''Fit a plateau and its standard deviation.'''
    df = spectra.dataframe[df_index]
    df_range = df[(df[df.columns[0]] >= cuts[0]) & (df[df.columns[0]] <= cuts[1])]
    x = df_range[df.columns[0]]
    y = df_range[df.columns[1]]

    if 'Error' in df_range.columns:

        error_range = df_range['Error']

        # Perform a weighted least squares fit
        degree = 1
        weights = 1.0 / error_range**2
        coefficients = np.polyfit(x, y, degree, w=weights)
        polynomial = np.poly1d(coefficients)

    else:
        # Perform a least squares fit
        degree = 1
        coefficients = np.polyfit(x, y, degree)
        polynomial = np.poly1d(coefficients)

    # Calculate the baseline
    baseline = polynomial(x)

    # Calculate the standard deviation of the residuals
    residuals = y - baseline
    error_std = np.std(residuals)

    baseline_value = np.mean(baseline)

    return baseline_value, error_std