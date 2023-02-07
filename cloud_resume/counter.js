 function getLoadCount(){

        // call an AWS gateway API, that then calls an AWS Lambda function
        // to read and then update AWS DynamoDB item showing load count

       
        var req = new XMLHttpRequest();  
        req.open('GET', 
        "https://g21z1pb3pa.execute-api.us-east-1.amazonaws.com/prod", 
        false);   
        req.send();  
        if(req.status == 200)
            {  
               var len = req.responseText.length;
            }
        else {
            // NOT OK response, so log in console
            console.log(req.status);
        }//end if
    }// end getLoadCount

    // read and write visit count into page, then increment count in DB
    window.onload = function(){

            // side effects
            // getLoadCount() updates field on page, increments count in DB
            getLoadCount();
        }; //end window.onload
