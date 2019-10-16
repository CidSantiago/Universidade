function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie(name) {   
    document.cookie = name+'=; Max-Age=-99999999;';  
}

function changeCSS(cssFile, cssLinkIndex) {

    if (cssFile==null) {
        return null;
    } else {
        var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);

        var newlink = document.createElement("link");
        newlink.setAttribute("rel", "stylesheet");
        newlink.setAttribute("type", "text/css");
        newlink.setAttribute("href", cssFile);
    
        document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
    
        setCookie("styleCookie",cssFile,7);
    }
    document.location.reload();
}

function changeFontSize(fontvar) {
    if (fontvar == 0) {
        document.body.style.fontSize = "12px";
        setCookie("fontCookie","12px",7);
    } else if(fontvar==null){
        return null;
    } else { 
    var refbody = document.body;
    var style = window.getComputedStyle(refbody);
    var fontSize = parseInt(style.getPropertyValue("font-size"));

    console.log(fontSize);

    document.body.style.fontSize = (fontSize + parseInt(fontvar)) + "px";
    
    setCookie("fontCookie",((fontSize + parseInt(fontvar))+"px"),7);
    }
    document.location.reload();
}

function showCookies(){
    var style = document.getElementById('style');
    var font = document.getElementById('font');

    style.innerHTML = getCookie("styleCookie");
    font.innerHTML = getCookie("fontCookie");
}

function updateCookies(){
 
    if (getCookie("styleCookie")!=null) {

        //Changing Style to cookie
        var oldlink = document.getElementsByTagName("link").item(0);
        var newlink = document.createElement("link");
        newlink.setAttribute("rel", "stylesheet");
        newlink.setAttribute("type", "text/css");
        newlink.setAttribute("href", "../"+getCookie("styleCookie"));
        document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
    }
    if (getCookie("fontCookie")!=null) {
    
        //Changing Font size to cookie
        var refbody = document.body;
        var style = window.getComputedStyle(refbody);
        document.body.style.fontSize = getCookie("fontCookie");
    }
}

function resetCookies(params) {
    eraseCookie("styleCookie");
    eraseCookie("fontCookie");
    eraseCookie("lastBook");
    document.location.reload();
}
window.onload = updateCookies;
