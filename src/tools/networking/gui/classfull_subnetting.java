/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tools.networking.gui;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;


/**
 *
 * @author Tony
 */

public class classfull_subnetting {
    private String ip, mask;
    private String out;
    private String[] info = new String[6];
    private String workingdir;

    classfull_subnetting(String ip, String mask){
        this.ip = ip;
        this.mask = mask;

        workingdir = System.getProperty("user.dir");
    }


    String check(){
         try {
            ProcessBuilder b = new ProcessBuilder("python", workingdir+"\\py\\check.py", ip, mask);//.inheritIO();
            Process p = b.start();
            out = new String(p.getInputStream().readAllBytes()); //redirect prints from python program to out
            return out; //error codes on check.py
            
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }


    String[] getinfo(){
        try {
            String[] temp ;

            ProcessBuilder b = new ProcessBuilder("python", workingdir+"\\py\\getinfo.py", ip, mask);//.inheritIO();
            Process p = b.start();
            out = new String(p.getInputStream().readAllBytes());
            temp=out.split("\\W{1,}"); //uses regex to split out
            
            for(int i=0; i<5; i++)
                info[i] = temp[i+1];
            
            info[5] = temp[6]+"."+temp[7]+"."+temp[8]+"."+temp[9];
            
            return info;
            
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }


    String[][] gen(){
        try{
            String[] temp ;
            String[][] list = new String[Integer.parseInt(info[3])][4]; //[number of subnets][subnetIP fromIP toIP broadcastIP]
            int t=1;
            
            ProcessBuilder b = new ProcessBuilder("python", workingdir+"\\py\\generate.py", info[0], info[1], info[2], info[3], info[4], info[5], ip, mask);//.inheritIO();
            Process p = b.start();
            out = new String(p.getInputStream().readAllBytes());
            temp=out.split("[^0-9.]{1,}"); //split in every not (number or .) 
            
            for(int i = 0; i< Integer.parseInt(info[3]); i++){ //insert temp into list
                for(int j =0; j<4; j++){
                    
                    list[i][j] = temp[t++];
                }
            }
            
            return list;
            
        }catch(IOException e){
            e.printStackTrace();
            return null;
        }
    }
    
    
    void writer(String path){
        
        try {
            
            String[] temp ;
            FileWriter wr = new FileWriter(path+"\\subnets.txt");
            
            try{ //Create file
            
            File outputf = new File(path+"\\subnets.txt");
            outputf.createNewFile();
            
            }catch(Exception e){}
            
            // Get INFO

            ProcessBuilder b = new ProcessBuilder("python", workingdir+"\\py\\getinfo.py", ip, mask);//.inheritIO();
            Process p = b.start();
            out = new String(p.getInputStream().readAllBytes());
            temp=out.split("\\W{1,}"); //uses regex to split out
            
            for(int i=0; i<5; i++)
                info[i] = temp[i+1];
            
            info[5] = temp[6]+"."+temp[7]+"."+temp[8]+"."+temp[9];
          
            //Write INFO
             try{//write to file
                

                wr.write("Mask Bits : "+ info[0]+"\n");
                wr.write("Host Bits : "+ info[1]+"\n");
                wr.write("Number of Subnets : "+ info[3]+"\n");
                wr.write("Hosts per Subnet : "+ info[4]+"\n");
                wr.write("Subnet Bit Mask : "+ info[5]+"\n\n");

            }catch(Exception e){}
             
            //Generate to file
            try{

                b = new ProcessBuilder("python", workingdir+"\\py\\generate.py", info[0], info[1], info[2], info[3], info[4], info[5], ip, mask);//.inheritIO();
                p = b.start();
                
                try{
                    wr.write(new String(p.getInputStream().readAllBytes()));                    
                }catch(Exception e){}
            }catch(IOException e){e.printStackTrace();}
            wr.close();
        } catch (IOException e) { e.printStackTrace();}
    }
}
//make a method that adds \n after ], on file export