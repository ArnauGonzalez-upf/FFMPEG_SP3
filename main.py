from sp3class import SP3Class

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get container
    cont = SP3Class()
    # Set selected value as one not in the range
    select = 100
    while select != "0":  # While to repeat until termination
        print("Select:")
        print("0) Exit")
        print("1) Convert Videos")
        print("2) Video Comparison")
        print("3) Video Streaming")
        print("4) Change IP")
        select = input()

        # Input options
        if select == "0":
            break
        elif select == "1":
            cont.convert_videos()
        elif select == "2":
            cont.video_comparison()
        elif select == "3":
            cont.video_streaming_send()
        elif select == "4":
            cont.change_ip()
        else:
            print("Not an option!")
