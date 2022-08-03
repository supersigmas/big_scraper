from twitchtube.video import make_video


make_video(
    #data=["c VALORANT", "game VALORANT"],
    data=["c VALORANT"],
    client_id="",  # example client id (fake)
    oauth_token="",  # example token (fake)
    video_length=2,
    resolution=(1080, 1920),
    frames=60,
)
