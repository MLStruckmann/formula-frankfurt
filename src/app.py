from maindash import app, server, recent_locations
from frontend.apps import main_app, detection_stream, track_visualization



if __name__ == '__main__':

    # Create video feed
    feed = detection_stream.serve_feed()

    # Create track visualization
    track_vis = track_visualization.layout()

    # Generate app layout
    app.layout = main_app.layout(video_feed = feed, 
                                 track_vis = track_vis,
                                 interval = 100)

    # Run app
    app.run_server(debug=True)
