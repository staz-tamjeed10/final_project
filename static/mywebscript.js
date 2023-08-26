let englishToFrench = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "englishToFrench?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
}

let frenchToEnglish = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "frenchToEnglish?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
}

let englishToUrdu = () => {
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "englishToUrdu?textToTranslate=" + textToTranslate, true);
    xhttp.send();
}

let urduToEnglish = () => {
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "urduToEnglish?textToTranslate=" + textToTranslate, true);
    xhttp.send();
}

let speechToText = () => {
    let audioFile = document.getElementById("audioFile").files[0];
    let formData = new FormData();
    formData.append('audio', audioFile);

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("recognized_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("POST", "speechToText", true);
    xhttp.send(formData);
}
