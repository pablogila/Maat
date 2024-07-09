from .core import *
from .fit import area_under_peak


def peaks_mapi(ins:Spectra,
         peaks:dict,
         df_index:int=0,
         ):
    '''
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

