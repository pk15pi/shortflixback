from django.db import models 

durationGroup = (
    ('below30s','below30s'),
    ('below1m','below1m'),
    ('below3m','below3m'),
    ('below5m','below5m'),
    ('below10m','below10m'),
    ('below20m','below20m'),
    ('below30m','below30m'),
    ('below1h','below1h'),
    ('below2h','below2h'),
    ('below5h','below5h'),
    ('above5h','above5h'),
)

class FormatChoice(models.Model):
    formatChoice = (
        ('MP4', 'MP4'),
        ('MP3', 'MP3'),
        ('FLV', 'FLV'),
        ('MOV', 'MOV'),
        ('AVI', 'AVI'),
        ('WMV ', 'WMV '),
        ('MKV ', 'MKV '),
        ('WebM', 'WebM'),
        ('3GP ', '3GP '),
        ('MPEG-2 ', 'MPEG-2 '),
        ('HEVC ', 'HEVC ')
    )
    name = models.CharField(choices=formatChoice, max_length=10, unique=True)


class GenreChoice(models.Model):
    genreChoice = (
        ('Action','Action'),
        ('Adventure','Adventure'),
        ('Comedy','Comedy'),
        ('Drama','Drama'),
        ('Horror','Horror'),
        ('Romance','Romance'),
        ('Sci-Fi','Sci-Fi'),
        ('Fantasy','Fantasy'),
        ('Thriller','Thriller'),
        ('Mystery','Mystery'),
        ('Documentary','Documentary'),
        ('Animation','Animation'),
        ('Musical','Musical'),
        ('Crime','Crime'),
        ('Historical','Historical'),
        ('Family','Family'),
        ('Sports','Sports'),
        ('Biographical','Biographical'),
        ('War','War'),
        ('Superhero','Superhero'),
        ('Family','Family'),
        ('Family','Family'),
        ('Family','Family'),
        ('Family','Family'),
        ('Family','Family')
    )
    name = models.CharField(choices=genreChoice, max_length=15, unique=True)


class Video(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the clip")
    subtitles = models.CharField(max_length=200, blank=True, help_text="Subtitles/Closed Captions: Availability of subtitles or closed captions and languages supported")
    file = models.FileField(upload_to='videos/', help_text="Video clip file")
    duration = models.CharField(max_length=50, blank=True, null=True, help_text="Duration of the clip")

    language = models.CharField(default='Hindi', max_length=20, help_text="The language spoken in the video or the primary language")
    native_language = models.CharField(default='English', max_length=20, help_text="Language of the movie / book first made / written")

    director = models.CharField(max_length=60, blank=True, help_text="Director of the movie")
    performers = models.CharField(max_length=60, blank=True, help_text="Main actors or individuals featured in the video (for movies, TV shows, etc.)")
    producer = models.CharField(max_length=60, blank=True, help_text="The producer or production company")
    location = models.CharField(max_length=60, blank=True, help_text="Where the video was filmed or the setting/context of the content")
    writer = models.CharField(max_length=60, blank=True, help_text="Author of the story")

    country_of_origin = models.CharField(max_length=25, blank=True, help_text="Where the book is written or movie is made")
    format = models.ManyToManyField(FormatChoice, related_name='format', help_text="select from drop down")
    genere = models.ManyToManyField(GenreChoice, related_name='genres', help_text="select from drop down")
    durationGroup = models.CharField(max_length=15, choices=durationGroup, blank=True, help_text="Grouping done based on duration of the clips like below 30 seconds, below 1 minutes etc")
    source = models.CharField(max_length=50, blank=True, help_text="Where the video came from (e.g., YouTube, Vimeo, self-uploaded)")

    resolution = models.CharField(max_length=5, blank=True, help_text="Resolutions of the clip")
    bitrate = models.CharField(blank=True, max_length=20, help_text="The data rate of the video, which affects video quality and file size")
    codec = models.CharField(blank=True, max_length=20, help_text="The video codec used for compression (e.g., H.264, HEVC, VP9)")
    audioCodec = models.CharField(blank=True, max_length=20, help_text="The codec used for audio (e.g., AAC, MP3, Opus)")
    audioChannels = models.CharField(blank=True, max_length=20, help_text="The number of audio channels (e.g., mono, stereo, 5.1 surround)")
    sampleRate = models.CharField(blank=True, max_length=20, help_text="The audio sample rate (e.g., 44.1 kHz, 48 kHz)")
    videoBitDepth = models.CharField(blank=True, max_length=20, help_text="The color depth of the video (e.g., 8-bit, 10-bit)")
    frameRate = models.TextField(blank=True, help_text="The number of frames per second (FPS) (e.g., 24fps, 30fps, 60fps)")
    aspectRation = models.TextField(blank=True, help_text="The aspect ratio of the video (e.g., 16:9, 4:3, etc.)")

    thumbnailImage = models.FileField(blank=True, upload_to='thumnails/', help_text="Image file to show as thumbnail image")
    previewClip = models.FileField(blank=True, upload_to='preview/', help_text="Short video file to show as thumbnail video")

    license = models.CharField(blank=True, max_length=50, help_text="The type of license (e.g., Creative Commons, All Rights Reserved, Public Domain)")
    copyright = models.TextField(blank=True, help_text="The entity or individual who holds the copyright")
    restrictions = models.TextField(blank=True, help_text="Usage Restrictions: Any restrictions on the use or distribution of the video clip")

    version = models.CharField(default='1', max_length=2, help_text="Version Number: If the video has been edited or updated, store version details")

    keyword = models.TextField(blank=True, help_text="Relevant tags or keywords that help in searching or categorizing the video")
    description = models.TextField(blank=True, help_text="A brief description of the video’s content or storyline")

    isMonetized = models.BooleanField(default=False, help_text="Whether the video is monetized (e.g., ads enabled, subscription content)")

    added_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def file_url(self):
        return self.file.url


class PlaybackInfo(models.Model):
    clip = models.ForeignKey(Video, related_name="video", on_delete=models.CASCADE)
    view = models.BigIntegerField(null=True)
    likes = models.BigIntegerField(null=True)
    dislikes = models.BigIntegerField(null=True)
    comment_count = models.BigIntegerField(null=True)


class Comments(models.Model):
    clip = models.ForeignKey(Video, related_name="commentfor", on_delete=models.CASCADE)
    comment = models.TextField()
    added_on = models.DateTimeField(auto_now=True)


class Monetization(models.Model):
    clip = models.ForeignKey(Video, related_name="moneyearned", on_delete=models.CASCADE)
    revenueGenerate = models.IntegerField(null=True, help_text="Revenue Generated: If the video is monetized, the revenue it has generated (if available).")

