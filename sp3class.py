import os


class SP3Class:
    # Define constructor
    def __init__(self):
        self.ip = '224.2.2.2'
        self.videos = ['BBB_CUT_720p', 'BBB_CUT_480p', 'BBB_CUT_320x240', 'BBB_CUT_160x120']

    def video_to_vp8(self):
        # Convert all videos to VP8
        for video in self.videos:
            cmd = 'ffmpeg -i ' + video + '.mp4 -c:v libvpx ' \
                  + video + '_vp8.webm '
            os.system(cmd)

    def video_to_vp9(self):
        # Convert all videos to VP9
        for video in self.videos:
            cmd = 'ffmpeg -i ' + video + '.mp4 -c:v libvpx-vp9 ' + video + '_vp9.webm'
            os.system(cmd)

    def video_to_h265(self):
        # Convert all videos to H265
        for video in self.videos:
            cmd = 'ffmpeg -i ' + video + '.mp4 -c:v libx265 ' \
                  + video + '_h265.mp4'
            os.system(cmd)

    def video_to_av1(self):
        # Select speed
        print("This encoder is very slow\nFast mode is avaliable (lower quality but faster encoding)\n"
              "Press 1 to use it")
        select = input()
        # Set speed
        if select == "1":
            cpu = '5'
        else:
            cpu = '1'
        # Convert all videos to AV1
        for video in self.videos:
            cmd = 'ffmpeg -i ' + video + '.mp4 -c:v libaom-av1 -cpu-used ' + cpu + ' ' + video + '_av1.mkv'
            os.system(cmd)

    def convert_videos(self):
        # Select option to convert
        print("Select:")
        print("1) VP8")
        print("2) VP9")
        print("3) H265")
        print("4) AV1")
        select = input()

        # Input options
        if select == "1":
            self.video_to_vp8()
        elif select == "2":
            self.video_to_vp9()
        elif select == "3":
            self.video_to_h265()
        elif select == "4":
            self.video_to_av1()
        else:
            print("Not an option!")

    @staticmethod
    def video_comparison():
        # Select video codec
        print("Select codec to use:")
        print("1) VP8")
        print("2) VP9")
        select = input()
        # Set video codec
        if select == "1":
            codec = 'libvpx'
        elif select == "2":
            codec = 'libvpx-vp9'
        else:
            print("Not an option!")
            return
        # Create video
        cmd = 'ffmpeg -i BBB_CUT_720p_vp8.webm -i BBB_CUT_720p_vp9.webm -filter_complex hstack -c:v '\
              + codec + ' vp8_vp9.webm'
        os.system(cmd)

    def video_streaming_send(self):
        # Emit video streaming
        cmd = 'ffmpeg -re -i BBB.mp4 -f mpegts udp://@' + self.ip + ':2222'
        os.system(cmd)

    def change_ip(self):
        # Select IP
        print("Select IP:")
        ip_selected = input()
        ip_selected_split = ip_selected.split(".")
        # Check if correct IP value
        for i in range(len(ip_selected_split)):
            value = int(ip_selected_split[i])
            if (len(ip_selected_split) != 4) or (i == 0 and not 224 <= int(ip_selected_split[0]) <= 239) or \
                    (value > 255 or value < 0):
                print("ERROR: IP range is between 224.0.0.0 and 239.255.255.255")
                return
        # Set IP
        self.ip = ip_selected
