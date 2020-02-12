from django.conf.urls import url

from . import views

urlpatterns = [
    # /app1
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^plot1d/$', views.Plot1DView.as_view(), name='plot1d'),
    url(r'^plot2d/$', views.Plot2DView.as_view(), name='plot2d'),
    url(r'^plot3d/$', views.Plot3DView.as_view(), name='plot3d'),
    url(r'^plot1d_multiple/(?P<n>\d+)/$',
        views.Plot1DMultipleView.as_view(), name='plot1d_multiple'),
    url(r'^plot1d_multiple_ajax/(?P<n>\d+)/$',
        views.plot1d_multiple_ajax, name='plot1d_multiple_ajax'),
    url(r'^plotIq/$', views.PlotIqView.as_view(), name='plotIq'),
    url(r'^plot_live/$', views.PlotLiveView.as_view(), name='plot_live'),
    url(r'^plot_live_update/$', views.plot_live_update, name='plot_live_update'),
    url(r'^prague/time/$', views.Plot3DScatterViewPragueTime.as_view(), name='plot3d_scatter_time_prague'),
    url(r'^spb/time/$', views.Plot3DScatterViewSpbTime.as_view(), name='plot3d_scatter_time_spb'),
    url(r'^prague/day_of_year/$', views.Plot3DScatterViewPragueDayOfYear.as_view(), name='plot3d_scatter_year_day_prague'),
    url(r'^spb/day_of_year/$', views.Plot3DScatterViewSpbDayOfYear.as_view(), name='plot3d_scatter_year_day_spb'),
    url(r'^prague/day_of_week/$', views.Plot3DScatterViewPragueDayOfWeek.as_view(), name='plot3d_scatter_week_day_prague'),
    url(r'^spb/day_of_week/$', views.Plot3DScatterViewSpbDayOfWeek.as_view(), name='plot3d_scatter_week_day_spb'),


]
