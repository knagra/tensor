%Author: Iwan Smith

%%Usage
%Instead of piping the output of main.c into krackoutput, send it to a
%file named out:
%./main > out

%Run this script in the same folder as the file out, and a window will pop
%up with an animation of the board. 

%It is currently rotated by 180 degrees. This could just be incorrect use
%of the image function


fid = fopen('out');

picture_data = zeros(18,64,3);
image_to_disp = zeros(24,48, 3);
while 1==1;
    
    for panel = 1:18;
        linedata = fgets(fid);
        picture_data(panel,:,2) = linedata(3:66);
        picture_data(panel,:,1) = linedata(67:130);
        picture_data(panel,:,3) = linedata(131:194);
    end
    
    panel=1;
    for pan_hor = 0:5;
        for pan_ver = 0:2;
            panel=pan_hor+1 + pan_ver*6;
            for line = 0:7;
                image_to_disp(pan_ver*8+line+1, pan_hor*8+1:pan_hor*8+8,:) = picture_data(panel,line*8+1:line*8+8,:);
                
            end
        end
    end
    
    image_to_disp = (image_to_disp-'0')/('F'-'0');
    image(image_to_disp);
    pause(0.05);
end
fclose(fid);
