import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import dash_table
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from datetime import datetime as dt
import json
import re
import datetime
import calendar
from datetime import date
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Demo'
df=pd.read_csv(r'data_processed.csv',
                index_col=["datetime"], 
                usecols=["datetime", "Platform Name","location","priority","monitoring item"],
                parse_dates=["datetime"])
df.index = pd.to_datetime(df.index)

today_date = datetime.datetime.today()
####past 6 months#######
six_months = date.today() + relativedelta(months=-5)
y6=six_months.month
z6=six_months.year
start_date_6=datetime.datetime(z6, y6, 2)

####past 2 months#######
last_month = date.today() + relativedelta(months=-1)
y1=last_month.month
z1=last_month.year
cal1=calendar.monthrange(z1,y1)
end_last_month=cal1[0]
start_date_1=datetime.datetime(z1, y1, 1)
end_date_1=datetime.datetime(z1, y1, end_last_month)

########################################################################### 
color_list1=['maroon','red','orange',
            'yellow','fuchsia','olive',
            'blue','green','purple',
            'gold','silver','gray',
            'black','greenyellow',
            'aqua','navy','lime',
            'firebrick','hotpink','chocolate',
            'rosybrown','darkviolet','honeydew',
            'ivory','magenta','moccasin'
            ]
color_list2=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
            'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
            'blueviolet', 'brown', 'burlywood', 'cadetblue',
            'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
            'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
            'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen',
            'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
            'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
            'darkslateblue', 'darkslategray', 'darkslategrey'
            # darkturquoise, darkviolet, deeppink, deepskyblue,
            # dimgray, dimgrey, dodgerblue, firebrick,
            # floralwhite, forestgreen, fuchsia, gainsboro,
            # ghostwhite, gold, goldenrod, gray, grey, green,
            # greenyellow, honeydew, hotpink, indianred, indigo,
            # ivory, khaki, lavender, lavenderblush, lawngreen,
            # lemonchiffon, lightblue, lightcoral, lightcyan,
            # lightgoldenrodyellow, lightgray, lightgrey,
            # lightgreen, lightpink, lightsalmon, lightseagreen,
            # lightskyblue, lightslategray, lightslategrey,
            # lightsteelblue, lightyellow, lime, limegreen,
            # linen, magenta, maroon, mediumaquamarine,
            # mediumblue, mediumorchid, mediumpurple,
            # mediumseagreen, mediumslateblue, mediumspringgreen,
            # mediumturquoise, mediumvioletred, midnightblue,
            # mintcream, mistyrose, moccasin, navajowhite, navy,
            # oldlace, olive, olivedrab, orange, orangered,
            # orchid, palegoldenrod, palegreen, paleturquoise,
            # palevioletred, papayawhip, peachpuff, peru, pink,
            # plum, powderblue, purple, red, rosybrown,
            # royalblue, saddlebrown, salmon, sandybrown,
            # seagreen, seashell, sienna, silver, skyblue,
            # slateblue, slategray, slategrey, snow, springgreen,
            # steelblue, tan, teal, thistle, tomato, turquoise,
            # violet, wheat, white, whitesmoke, yellow,
            # yellowgreen
            ]
###########################################################################

Title = 'Alert Analysis'
app.layout = html.Div([

    

    html.Div([
            html.H3('Alert Analysis Report'),
    ],style={'text-align': 'center'}),

    html.Div([
            html.Div([

            dcc.DatePickerRange(
            id='my-date-picker-range-slack',
            #min_date_allowed=dt(2019, 9, 1),
            #max_date_allowed=dt(2025, 9, 1),
            initial_visible_month=dt(2019, 9, 2),
            calendar_orientation ='horizontal',
            start_date=start_date_6,
            end_date=today_date,
            ),
            html.Div(id='output-container-date-picker-range-slack'),

            html.Br(),
            html.Label('Select trend'),
            dcc.Dropdown(id='dropdown-slack-trend',
                    options=[
                            {'label': 'Monthly', 'value': 'month'},
                            {'label': 'Weekly', 'value': 'week'},
                            {'label': 'Daily', 'value': 'day'},
                            ],
                    value='month'
                            ),
            html.Br(),
            html.Label('Select channel'), 
                      
                dcc.Dropdown(id='dropdown-slack-channel',
                    options=[
                            {'label': 'Summary Dashboard', 'value': 'dashboard'},
                            {'label': 'Platform 1', 'value': 'platform 1'},
                            {'label': 'Platform 2', 'value': 'platform 2'},
                            {'label': 'Platform 3', 'value': 'platform 3'},
                            {'label': 'Platform 4', 'value': 'platform 4'},
                            {'label': 'Platform 5', 'value': 'platform 5'},
                            {'label': 'Platform 6', 'value': 'platform 6'},
                            {'label': 'Platform 7', 'value': 'platform 7'},
                            {'label': 'Platform 8', 'value': 'platform 8'},
                            {'label': 'Platform 9', 'value': 'platform 9'},
                            {'label': 'Platform 10', 'value': 'platform 10'},
                            {'label': 'Platform 11', 'value': 'platform 11'},
                            {'label': 'Platform 12', 'value': 'platform 12'},
                            {'label': 'Platform 13', 'value': 'platform 13'},
                            {'label': 'Platform 14', 'value': 'platform 14'},
                            {'label': 'Platform 15', 'value': 'platform 15'},
                            ],
                    value='dashboard'
                                ),
                            html.Br(),
                html.Label('Filter location (exclude from data)'),                 
                dcc.Dropdown(id='checklist-slack',
                            multi=True
                                ),
                 
                             html.Br(),
                html.Label('Filter location (exclude from data)'),                 
                dcc.Checklist(id='checklist-compare',
                                options=[
                                {'label': 'Comparison', 'value': 'compare'},
                                ],
                                ) 
                                                               

            ],className='two columns',style={'height':'1000px','padding': 10,'background-color':'lightblue'}),                          


                
                html.Div([
                        dcc.Graph(
                        id='graph1-slack',
                        clear_on_unhover=True,
                        className='six columns'
                        ),
                         dcc.Graph(
                        id='graph2-slack',
                        clear_on_unhover=True,
                        className='six columns'
                        ),           

                ],className='ten columns',style={'padding': 10}),
                html.Div([
                        dcc.Graph(
                        id='graph3-slack',
                        clear_on_unhover=True,
                        className='six columns'
                        ),
            
                        dcc.Graph(
                        id='graph4-slack',
                        clear_on_unhover=True,
                        className='six columns'
                        ),                        
                ],className='ten columns',
                    #style={'padding': 10,}
                    ),
                
                html.Div(children=html.Div(id='graphs')),

                # html.Div([
                #         dcc.Textarea(
                #         id='text1-slack',
                #         value='Executive Summary',
                #         style={'height': '80%'},
                #         rows=20,
                #         disabled='true',
                #         className='six columns'
                #         )],style={'padding': 10,'margin-left': '30px'}),

    ])
],style={'padding': 30},)

@app.callback(
    dash.dependencies.Output('output-container-date-picker-range-slack', 'children'),
    [dash.dependencies.Input('my-date-picker-range-slack', 'start_date'),
     dash.dependencies.Input('my-date-picker-range-slack', 'end_date')])

def update_output(start_date, end_date):

    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date = dt.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        #start_date = start_date.strptime('%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date = dt.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix

@app.callback(
    dash.dependencies.Output('checklist-slack', 'options'),
    [dash.dependencies.Input('dropdown-slack-channel', 'value')])

def checklist_update(value):

    if value is None:
        raise PreventUpdate

    elif value=='dashboard':
        location=df['location'].unique()
        options=[{'label': i, 'value': i} for i in location]
    else:
        df_platform_name=df[df['Platform Name']==value]
        location=df_platform_name['location'].unique()
        options=[{'label': i, 'value': i} for i in location]
    return options

@app.callback(
    [dash.dependencies.Output('graph1-slack', 'figure'),
    dash.dependencies.Output('graph2-slack', 'figure'),
    dash.dependencies.Output('graph3-slack', 'figure'),
    dash.dependencies.Output('graph4-slack', 'figure')],
    [dash.dependencies.Input('dropdown-slack-trend', 'value'),
    dash.dependencies.Input('my-date-picker-range-slack', 'start_date'),
    dash.dependencies.Input('my-date-picker-range-slack', 'end_date'),
    dash.dependencies.Input('checklist-slack', 'value'),
    dash.dependencies.Input('dropdown-slack-channel', 'value'),
    dash.dependencies.Input('graph1-slack','hoverData'),
    dash.dependencies.Input('graph2-slack','hoverData'),
    dash.dependencies.Input('graph3-slack','hoverData'),
    dash.dependencies.Input('graph4-slack','hoverData')])

def update_chart1(value,start_date, end_date,
                    checklist_slack_val,dropdown_slack_val,
                    hoverData1,hoverData2,hoverData3,hoverData4):
    # print(start_date)
    # print(df.head())
    #platform selection   

    if dropdown_slack_val=='dashboard':
        df1=df
    else:
        df1=df[df['Platform Name']==dropdown_slack_val]

    #unselect location from database
    if checklist_slack_val is not None:
        df_unselect = df1[~df1['location'].isin(checklist_slack_val)]
    else:
        df_unselect=df1

    if value is None:
        raise PreventUpdate
    elif value=='month':

        if hoverData1 is not None:    
            data1=hoverData1['points'][0]['x']
            print(data1)
            data1_date=dt.strptime(data1,"%b-%y")
            z=data1_date.year
            y=data1_date.month
            cal=calendar.monthrange(z,y)
            end_month=cal[1]
            start_date=datetime.datetime(z, y, 1)
            end_date=datetime.datetime(z, y, end_month)
            print(start_date)
            print(end_date)
            #current_month_start=

        df2 = df_unselect[(df_unselect.index >= start_date) & (df_unselect.index <= end_date)] 
        table_data=df2.resample('M').count()
        table_data['month_year']=table_data.index.strftime("%b-%y")
        x=table_data['month_year']
        string="Incident Monthly Trend"
        chart_type='bar'
            

        df3=df2.groupby('location').count()
        df3.sort_values('Platform Name',ascending=False)

        if dropdown_slack_val=='dashboard':
            # print(df2)
            # print(table_data.iloc[0])
            # print(table_data.iloc[1])
            df4=df2.groupby('Platform Name').count()
            df4=df4.sort_values('location',ascending=True)
        else:
            df4=df2.groupby('monitoring item').count()
            df4=df4.sort_values('location',ascending=True).head(10)             

        df5=df2.groupby('priority').count()
        df5=df5.sort_values('location',ascending=True)
       

    elif value=='week':
        df2 = df_unselect[(df_unselect.index >= start_date) & (df_unselect.index <= end_date)]
        table_data=df2.resample('W').count()
        table_data['month_year']="Week " + table_data.index.strftime("%W")
        x=table_data['month_year']
        string="Incident Weekly Trend"
        chart_type='bar'

        df3=df2.groupby('location').count()
        df3.sort_values('Platform Name',ascending=False)

        if dropdown_slack_val=='dashboard':
            df4=df2.groupby('Platform Name').count()
            df4=df4.sort_values('location',ascending=True)
        else:
            df4=df2.groupby('monitoring item').count()
            df4=df4.sort_values('location',ascending=True).head(10)  

        df5=df2.groupby('priority').count()
        df5=df5.sort_values('location',ascending=True)

    elif value=='day':
        df2 = df_unselect[(df_unselect.index >= start_date) & (df_unselect.index <= end_date)]
        table_data=df2.resample('D').count()
        table_data['month_year']=table_data.index.strftime("%Y-%m-%d")
        x=table_data['month_year']
        string="Incident Daily Trend"
        chart_type='line'

        df3=df2.groupby('location').count()
        df3.sort_values('Platform Name',ascending=False)

        if dropdown_slack_val=='dashboard':
            df4=df2.groupby('Platform Name').count()
            df4=df4.sort_values('location',ascending=True)
        else:
            df4=df2.groupby('monitoring item').count()
            df4=df4.sort_values('location',ascending=True).head(10) 

        df5=df2.groupby('priority').count()
        df5=df5.sort_values('location',ascending=True)
    ###################################################

    figure1={
            'data': [
                {'x': x, 
                'y': table_data['monitoring item'], 
                'type': chart_type,
                'color':x,
                'marker':dict(color=color_list1),},
            ],
            'layout': {
                'title': string,
                'clickmode': 'event+select'
                #'showlegend':True
                }
            }
    
    figure2={
            'data' : [{'type' : 'pie',
                'name' : "Students by level of study",
                'labels' : df3.index,
                'values' : df3['Platform Name'],
                'direction' : 'clockwise',
                'hoverinfo': 'none',
                'hole':0.3}],
            'layout': {
                'title': string,
                'clickmode': 'event+select'
                #'showlegend':True
                }
            } 

    figure3={
            'data' : [go.Bar(
                x=df4['location'],
                y=df4.index,
                orientation='h',
                marker=dict(color=color_list1)
            )],
            'layout': {
                'title': string,
                'clickmode': 'event+select'
                #'showlegend':True
                }
            }    

    figure4={
            'data' : [{'type' : 'pie',
                'name' : "Students by level of study",
                'labels' : df5.index,
                'values' : df5['location'],
                'direction' : 'clockwise',
                'hoverinfo': 'none',
                'hole':0.3}],
            'layout': {
                'title': string,
                'clickmode': 'event+select'
                #'showlegend':True
                }
            } 

    return  figure1,figure2,figure3,figure4

@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('checklist-compare', 'value')]
            )

def update_compare(checklist_val):

    if checklist_val is None or not checklist_val:
        graphs=""
        print(checklist_val)

    # if not checklist_val:
    #     print(checklist_val)
        
 #       print(checklist_val[0])
    elif checklist_val[0]=='compare':
        print('yes')
        graphs= html.Div([
                html.Div([
                           
                dcc.Graph(
                id='test',
                className='six columns',
                figure={
                'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                'title': 'Dash Data Visualization'
                }
                }
                ),
                dcc.Graph(
                id='tes2',
                className='six columns',
                figure={
                'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                'title': 'Dash Data Visualization'
                }
                }
                ),
                ])
        ],className='ten columns')

    return graphs
        
if __name__ == '__main__':
    app.run_server()
