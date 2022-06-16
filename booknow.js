//to disable prev dates
var today = new Date().toISOString().split('T')[0];
document.getElementsByName("Date")[0].setAttribute('min', today);

//prefernces drop-down
function populate(s1,s2) {
    var s1=document.getElementById(s1);
    var s2=document.getElementById(s2);

    s2.innerHTML = "";

    if(s1.value == "staycation"){
        var optionArray =['heritage resort coorg|Heritage Resort Coorg','allaranda luxury villa|Allaranda Luxury Villa','the serai|The Serai',
                          'vismita country|Vismita Country','swaswara|Swaswara','palm meadows club|Palm Meadows Club',
                          'evolve back hampi|Evolve Back Hampi','the bison resort|The Bison Resort','coorg wilderness resort|Coorg Wilderness Resort'];
    }
    else if(s1.value == "trekking"){
        var optionArray =['kudremukh|Kudremukh','kodachadri|Kodachadri','tadiandamol|Tadiandamol',
                           'galibeedu|Galibeedu','mullayanagiri|Mullayanagiri','skandagiri|Skandagiri',
                           'bandaje arbi|Bandaje Arbi','yana|Yana','savandurga|Savandurga'];
    }
    else if(s1.value == "tranquility"){
        var optionArray =['abbey falls|Abbey Falls','unchalli falls|Unchalli Falls','shivana samudra|Shivana Samudra',
                          'sathodi falls|Sathodi Falls','gokak falls|Gokak Falls','hogenakkal falls|Hogenakkal Falls',
                          'jog falls|Jog Falls','hebbe falls|Hebbe Falls','magod falls|Magod Falls'];
    }
    else if(s1.value == "historical places"){
        var optionArray =['stone chariot|Stone Chariot','jalasangvi|Jalasangvi','halebeedu|Halebeedu',
                          'hampi|Hampi','aihole|Aihole','badami|Badami',
                          'basavakalyan|Basavakalyan','beluru|Beluru','ashtoor|Ashtoor'];
    }
    else if(s1.value == "beaches"){
        var optionArray =['om beach|Om Beach','panambur beach|Panambur Beach','kudle beach|Kudle Beach',
                          'paradise beach|Paradise Beach','tannirbhavi beach|Tannirbhavi Beach','devbagh beach|Devbagh Beach',
                          'padubidri beach|Padubidri Beach','kasargod beach|Kasargod Beach','malpe beach|Malpe Beach'];
    }
    else if(s1.value == "wildlife"){
        var optionArray =['gudekote sloth bear sanctuary|Gudekote Sloth Bear Sanctuary','mookambika wildlife sanctuary|Mookambika Wildlife Sanctuary','Sharavathi wildlife sanctuary|Sharavathi Wildlife Sanctuary',
                          'someshwara wildlife sanctuary|Someshwara Wildlife Sanctuary','bhadra wildlife sanctuary|Bhadra Wildlife Sanctuary','bhimgad wildlife sanctuary|Bhimgad Wildlife Sanctuary',
                          'b r tiger reserve and wildlife |B R Tiger Reserve and Wildlife ','daroji sloth bear sanctuary|Daroji Sloth Bear Sanctuary','kali tiger reserve|Kali Tiger Reserve'];
    }

    for(var option in optionArray){
        var pair = optionArray[option].split("|");
        var newoption = document.createElement("option");

        newoption.value = pair[0];
        newoption.innerHTML = pair[1];
        s2.options.add(newoption);
    }
}

function clickme(){
    swal("Booked Successfully!", "Our team will reach you out soon.", "success");
}
