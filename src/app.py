from maindash import app, get_config
from frontend.apps import main_app, detection_stream, track_visualization, high_score_table, race_management_frontend

from azure_.az_storage.cosmos_data import download_cosmos #TODO replace with real azure

import json


if __name__ == '__main__':

    config = get_config()

    # Get high score data from Azure
    hs_df = download_cosmos(config['azure_cosmos_key'])

    # Create high score table
    hs_table = high_score_table.layout(hs_df)

    # Create video feed
    feed = detection_stream.serve_feed()

    # Create track visualization
    track_vis = track_visualization.layout(config['aspect_ratio'])

    # Create Race Management Frontend
    rm_form = race_management_frontend.rm_form()

    # Generate app layout
    app.layout = main_app.layout(video_feed = feed, 
                                 track_vis = track_vis,
                                 high_score_table = hs_table,
                                 rm_form = rm_form,
                                 interval = 50)

    # Run app
    app.run_server(debug=True)
