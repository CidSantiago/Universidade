function changeCSS(cssFile, cssLinkIndex) {

    var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);

    var newlink = document.createElement("link");
    newlink.setAttribute("rel", "stylesheet");
    newlink.setAttribute("type", "text/css");
    newlink.setAttribute("href", cssFile);

    document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
    }

function changeFontSize(fontvar) {
    if (fontvar == 0) {
        document.body.style.fontSize = "12px";
    } else { 
    var refbody = document.body;
    var style = window.getComputedStyle(refbody);
    var fontSize = parseInt(style.getPropertyValue("font-size"));

    console.log(fontSize);

    document.body.style.fontSize = (fontSize + parseInt(fontvar)) + "px";
   
    }

}

