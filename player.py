from torrent.torrentz import torrent_api
import subprocess,sys
def main():
      
    
    try:  
        results = torrent_api()
       
        magnets = []
        for key, value in results.items():
            magnets.append(value[5])
            print(f"⭐{key} {value[0]} >> |Leeches:{value[1]}| |Seeds:{value[2]}| |Size:{value[3]}| |Last Updated:{value[4]}| \n\n") 
            
        mv_choice = int(input("Enter the index of the movie which you want to stream/download: "))
        magnet_link = magnets[mv_choice-1]
        download = False # Default is streaming
        stream_choice = int(input("Press 1 to stream or Press 2 to download the movie: "))
        if stream_choice == 2:
            download = True

        webtorrent_stream(magnet_link,download)
        
    except Exception as e:
        print('Error:', e)


# Handle Streaming
def webtorrent_stream(magnet_link,download):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    if not download:
        cmd.append('--vlc')
    
    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd,shell=True)



if __name__ == "__main__":
    main()