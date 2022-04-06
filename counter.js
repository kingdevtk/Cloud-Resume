var url = "https://g21z1pb3pa.execute-api.us-east-1.amazonaws.com/prod";

var xhr = new XMLHttpRequest();
xhr.open("GET", url);

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
      console.log(xhr.status);
      console.log(xhr.responseText);
   }};

xhr.send();

