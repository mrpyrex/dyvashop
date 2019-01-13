// Initialize paystack object
var paystack;
Paystack.init({
  form: "paystack-card-form", // Form ID
  access_code: 'd5gtr5gnex'   // You should programmatically pass the access
                              // code via Ajax or a server variable. Note that
                              // the access code can only be used once. 
}).then(function(returnedObj){
  paystack = returnedObj;
}).catch(function(error){
  console.log("There was an error loading Paystack", error);
});

$("#paystack-card-form").submit(function(e){
    e.preventDefault();
    // You are to programmatically pass the pin provided by your custoemr
    // to this function
    // It gets all the card fields from the data-paystack input fields
    paystack.card.charge({
      pin: readPin() // Called a function that returns the optional pin value
    }).then(function(response){
      console.log(response);
    }, function(error){
      console.log(error);
    });
  });