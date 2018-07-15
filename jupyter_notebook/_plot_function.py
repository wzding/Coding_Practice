import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def histogram(df_list, label_list, title="?", xlabel="?", ylabel="?"):
    fig = plt.figure(1, figsize=(8, 6))
    plt.hist(df_list, label=label_list, alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    return


def boxplot_column(df, column_target, column_groupby, day="no"):
    '''
    boxplot
    '''
    pplt = df[[column_target, column_groupby]].boxplot(
        by=column_groupby, figsize=(12, 6), rot=45)
    if "day" == "yes":
        day_list = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
        pplt.set_xticklabels(day_list)
    pplt.set_xlabel(column_groupby)
    pplt.set_ylabel(column_target)
    pplt.set_title("distribution of %s by %s" %
                   (column_target, column_groupby))
    return


def lineplot(df, column1, column2, m="o", title="?", xlabel="?", ylabel="?", xticks=None):
    '''
    line plot
    '''
    pplt = df[[column1, column2]].plot(marker=m, figsize=(12, 6))
    pplt.set_title(title)
    # pplt.set_title("%s and %s of %s" % (column1, column2, ylabel))
    pplt.set_xlabel(xlabel)
    if xticks:
        pplt.set_xticks(range(len(df[xticks])))
        pplt.set_xticklabels(df[xticks])
    pplt.set_ylabel(ylabel)
    for tick in pplt.get_xticklabels():
        tick.set_rotation(45)
    return


def lineplot_time_related(df, column_time, column_target, day="no",
                          m="o", line="-"):
    '''
    time series plot
    '''
    temp = df.sort_values(column_time)
    pplt = temp.set_index(column_time)[column_target].plot(
        marker=m, ls=line, figsize=(12, 6))
    if "day" == "yes":
        day_list = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
        pplt.set_xticklabels(day_list)
    pplt.set_xlabel(column_time)
    pplt.set_ylabel(column_target)
    pplt.set_title("%s by %s" % (column_target, column_time))
    return


#################### the following plots need maps
#################### the following plots need maps
#################### the following plots need maps
def plot_legs(df, dst_dir, title="?", boundary="all"):
    '''
    plot all legs in df on a map, df should have columns: 'latitude_x',
    'longitude_x', 'latitude_y' and 'longitude_y'
    '''
    fig = plt.figure(1, figsize=(16, 12))
    # setup mercator map projection.
    if boundary == "domestic":
        m = Basemap(llcrnrlon=-126, llcrnrlat=23.5, urcrnrlon=-65,
                    urcrnrlat=50, projection='merc')
    else:
        m = Basemap(llcrnrlon=-150, llcrnrlat=-35, urcrnrlon=136,
                    urcrnrlat=62, projection='merc')

    m.drawmapboundary(fill_color='#EBF4FA')
    m.drawcoastlines()
    m.fillcontinents()
    m.drawcountries()
    # m.drawcounties(linewidth= 0.15, color= '#000066')
    m.drawstates(linewidth=1.2, linestyle='solid', color='w')
    m.drawparallels(np.arange(15, 60, 15), labels=[1, 1, 1, 1])
    m.drawmeridians(np.arange(-120, -50, 40), labels=[1, 1, 1, 1])
    plt.title(title, fontsize=20)

    for index, row in df.iterrows():
        Dep_lat = row['latitude_x']
        Dep_lon = row['longitude_x']
        Arr_lat = row['latitude_y']
        Arr_lon = row['longitude_y']
        # draw great circle route between NY and London
        m.drawgreatcircle(Dep_lon, Dep_lat, Arr_lon, Arr_lat, del_s=10,
                          alpha=0.7, linestyle='solid')
    fig.savefig(dst_dir + "legs_" + "%s" % boundary + ".png", dpi=150)
    fig.clear()
    return


def plot_ports_by_freq(df, dst_dir, threshold=500, port_type="Orign",
                       boundary="domestic"):
    """
    plot either orign or destination ports by frequency on a map
    frequent ports are shown in red, while less frequent ones shown in blue
    """
    fig = plt.figure(1, figsize=(16, 12))
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, 2)]
    # setup mercator map projection.
    if boundary == "domestic":
        m = Basemap(llcrnrlon=-126, llcrnrlat=23.5, urcrnrlon=-65,
                    urcrnrlat=50, projection='merc')
    else:
        m = Basemap(llcrnrlon=-150, llcrnrlat=-35, urcrnrlon=136,
                    urcrnrlat=62, projection='merc')
    m.drawmapboundary(fill_color='#EBF4FA')
    m.drawcoastlines()
    m.fillcontinents()
    m.drawcountries()
    m.drawstates(linewidth=1.2, linestyle='solid', color='w')
    m.drawparallels(np.arange(15, 60, 15), labels=[1, 1, 1, 1])
    m.drawmeridians(np.arange(-120, -50, 40), labels=[1, 1, 1, 1])

    if boundary == "domestic":
        plt.title("%s Ports(Domestic)" % port_type, fontsize=20)
    elif boundary == "international":
        plt.title("%s Ports(International)" % port_type, fontsize=20)
    else:
        plt.title("%s Ports" % port_type, fontsize=20)

    freq = df[df.sample_size > threshold]
    non_freq = df[df.sample_size <= threshold]

    if port_type == "Orign":
        for index, row in non_freq.iterrows():
            lat = row['latitude_x']
            lon = row['longitude_x']
            m.plot(lon, lat, color=colors[1], marker='.',
                   alpha=0.7,  latlon=True)
        for index, row in freq.iterrows():
            lat = row['latitude_x']
            lon = row['longitude_x']
            m.plot(lon, lat, color=colors[0], marker='.',
                   alpha=0.7, latlon=True)
    else:
        for index, row in non_freq.iterrows():
            lat = row['latitude_y']
            lon = row['longitude_y']
            m.plot(lon, lat, color=colors[1], marker='.',
                   alpha=0.7, latlon=True)
        for index, row in freq.iterrows():
            lat = row['latitude_y']
            lon = row['longitude_y']
            m.plot(lon, lat, color=colors[0], marker='.',
                   alpha=0.7, latlon=True)
    fig.savefig(dst_dir + "%s_" % port_type + "%s" % boundary + ".png",
                bbox_inches='tight', dpi=150)
    fig.clear()
    return


def plot_all_ports_by_freq(OO, DD, dst_dir, boundary="domestic"):
    """
    plot both origin and destination ports by frequency on a map
    size of circle represents frequency
    """
    fig = plt.figure(1, figsize=(16, 12))
    colors = [plt.cm.bwr(each) for each in np.linspace(0, 1, 2)]
    # setup mercator map projection.
    if boundary == "domestic":
        m = Basemap(llcrnrlon=-126, llcrnrlat=23.5, urcrnrlon=-65,
                    urcrnrlat=50, projection='merc')
    else:
        m = Basemap(llcrnrlon=-150, llcrnrlat=-35, urcrnrlon=136,
                    urcrnrlat=62, projection='merc')
    m.drawmapboundary(fill_color='#EBF4FA')
    m.drawcoastlines()
    m.fillcontinents()
    m.drawcountries()
    m.drawstates(linewidth=1.2, linestyle='solid', color='w')
    m.drawparallels(np.arange(15, 60, 15), labels=[1, 1, 1, 1])
    m.drawmeridians(np.arange(-120, -50, 40), labels=[1, 1, 1, 1])

    if boundary == "domestic":
        plt.title("Ports(Domestic)", fontsize=20)
    elif boundary == "international":
        plt.title("Ports(International)", fontsize=20)
    else:
        plt.title("Origin and Destination Ports", fontsize=20)

    for index, row in OO.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        m.plot(lon, lat, color=colors[0], marker='.',
               markersize=np.sqrt(row.sample_size), alpha=0.7, latlon=True)
    for index, row in DD.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        m.plot(lon, lat, color=colors[1], marker='.',
               markersize=np.sqrt(row.sample_size), alpha=0.7, latlon=True)
    fig.savefig(dst_dir + "Ports_" + "%s" % boundary + ".png",
                bbox_inches='tight', dpi=150)
    fig.clear()
    return


def plot_port_by_mot(df_list, mode_list):
    '''
    plot both origin and destination ports by each mode on a map
    size of circle represents frequency
    '''
    for i in range(len(mode_list)):
        OO = pd.DataFrame(df_list[i].groupby([
            "origin", "domestic_x", "latitude_x", "longitude_x"])[
            "sample_size"].sum().reset_index())
        DD = pd.DataFrame(df_list[i].groupby([
            "destination", "domestic_y", "latitude_y", "longitude_y"])[
            "sample_size"].sum().reset_index())
        fig = plt.figure(1, figsize=(16, 12))
        colors = [plt.cm.bwr(each) for each in np.linspace(0, 1, 2)]
        # setup mercator map projection.
        m = Basemap(llcrnrlon=-126, llcrnrlat=23.5, urcrnrlon=-65,
                    urcrnrlat=50, projection='merc')
        m.drawmapboundary(fill_color='#EBF4FA')
        m.drawcoastlines()
        m.fillcontinents()
        m.drawcountries()
        m.drawstates(linewidth=1.2, linestyle='solid', color='w')
        m.drawparallels(np.arange(15, 60, 15), labels=[1, 1, 1, 1])
        m.drawmeridians(np.arange(-120, -50, 40), labels=[1, 1, 1, 1])

        plt.title("Origin & Destination Ports(%s)" %
                  str(mode_list[i]), fontsize=20)
        for index, row in OO.iterrows():
            lat = row['latitude_x']
            lon = row['longitude_x']
            m.plot(lon, lat, color=colors[0], marker='.', alpha=0.5,
                   markersize=np.sqrt(row.sample_size), latlon=True)
        for index, row in DD.iterrows():
            lat = row['latitude_y']
            lon = row['longitude_y']
            m.plot(lon, lat, color=colors[1], marker='.', alpha=0.5,
                   markersize=np.sqrt(row.sample_size), latlon=True)
        fig.savefig("Ports_" + "%s" % mode_list[i] + ".png",
                    bbox_inches='tight', dpi=150)
        fig.clear()
    return
