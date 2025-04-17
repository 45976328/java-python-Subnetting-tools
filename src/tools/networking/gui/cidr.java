package tools.networking.gui;

import java.util.*;

public class cidr {

    List<Integer> ip = new ArrayList<>();
    List<Integer> mask = new ArrayList<>();
    
    List<String> ip_bin = new ArrayList<>();
    List<String> mask_bin = new ArrayList<>();

    cidr(String ip, String mask){
        
        String[] temp= ip.split("\\.");
        
        for (String t : temp) this.ip.add(Integer.valueOf(t));

        temp = mask.split("\\.");
        
        for(String t : temp) this.mask.add(Integer.valueOf(t));
        
    }


    String check (){
        
        if (ip.size() != 4)
            return "Wrong Size of IP";
        
        if (mask.size() !=4)
            return "Wrong Size of Mask";
        
        for(int i=1; i<4; i++)
            if( mask.get(i-1) != 255 && ( mask.get(i) < 0 ||  mask.get(i) > 255  ) || mask.get(3) > 252 )
                return "Wrong Mask Format";
        
        for(int i=0; i<4; i++)
            if(ip.get(i) < 0 || ip.get(i) > 255)
                return "IP out of Boundaries";

        
        tobin();

        String temp = mask_bin.get(0)+mask_bin.get(1)+mask_bin.get(2)+mask_bin.get(3);

        if(temp.contains("01"))
            return "Wrong Mask Value";        
                           
        return "";
    }

    void tobin(){
        
        String front = "", back = "";

        for(int i=0; i<4; i++){

            back=Integer.toBinaryString(ip.get(i));

            for(int j=0; j< 8-back.length(); j++ ) //add 8- length of binip[i] zeroes in front
                    front+="0";

            ip_bin.add(front+back);

            front = "";
            back = "";

            back=Integer.toBinaryString(mask.get(i));

            for(int j=0; j< 8-back.length(); j++ )
                    front+="0";

            mask_bin.add(front+back);

            front = "";
            back = "";

        }
    }


    String generate(){
        
        String subnet="", from="", to="", broadcast="";

        List<Integer> wildcard = new ArrayList<>();

        for(int i=0; i<3; i++)
            subnet+= Integer.toString(ip.get(i) & mask.get(i))+".";

        subnet+= Integer.toString(ip.get(3) & mask.get(3));

        for(int i=0; i<3; i++)
            from += Integer.toString(ip.get(i) & mask.get(i))+".";
        
        from += Integer.toString( (ip.get(3) & mask.get(3)) + 1);

        //find the wildcard of mask and do bitwise OR between ip and mask
        for(int i=0; i<4; i++)
            wildcard.add(255-mask.get(i));

        for(int i=0; i<3; i++)
            broadcast += Integer.toString(ip.get(i) | wildcard.get(i)) + ".";

        broadcast += Integer.toString(ip.get(3) | wildcard.get(3));

        for(int i=0; i<3; i++)
            to += Integer.toString(ip.get(i) | wildcard.get(i)) + ".";
        
        to += Integer.toString( (ip.get(3) | wildcard.get(3)) -1 );

        return subnet + "\t\t  " + from + "   to   " + to + " \t\t  " + broadcast;
    }
}
