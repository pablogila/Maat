from .common import *


def mdataset(mdata:MData):
    
    if mdata.figsize:
        fig, ax = plt.subplots(figsize=mdata.figsize)
    else:
        fig, ax = plt.subplots()

    if mdata.low_xlim:
        ax.set_xlim(left=mdata.low_xlim)
    if mdata.top_xlim:
        ax.set_xlim(right=mdata.top_xlim)
    if mdata.low_ylim:
        ax.set_ylim(bottom=mdata.low_ylim)
    if mdata.top_ylim:
        ax.set_ylim(top=mdata.top_ylim)

    if ins.scale_range:
        scale_factor = ins.scale_range
        df0 = ins.dataframes[0]
        df0 = df0[(df0[df0.columns[0]] >= ins.scale_range[0]) & (df0[df0.columns[0]] <= ins.scale_range[1])]
        max_df = df0[df0.columns[1]].max()
        ax.set_ylim(top=ins.scale_y*max_df)

    strings_to_delete_from_name = ['.csv', '_INS', '_temp']
    for df, name in zip(ins.dataframes, ins.filenames):
        if ins.scale_range:
            first_cut = ins.scale_range[0]
            second_cut = ins.scale_range[1]
            df_range_i = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            max_df_i = df_range_i[df_range_i.columns[1]].max()
            df[df.columns[1]] = max_df * (df[df.columns[1]] / max_df_i)
        
        if (ins.y_offset is True) and (ins.y_low_lim is not None) and (ins.y_top_lim is not None):
            number_of_plots = len(ins.dataframes)
            height = ins.y_top_lim - ins.y_low_lim
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (ins.filenames.index(name) * height) / number_of_plots

        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if ins.legend and isinstance(ins.legend, list):
            name_clean = ins.legend[ins.filenames.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    plt.title(ins.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if ins.log_xscale:
        ax.set_xscale('log')
    if not ins.show_yticks:
        ax.set_yticks([])
    if ins.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if ins.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, ins.save_as)
        plt.savefig(save_name)
    
    plt.show()

