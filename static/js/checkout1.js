$(document).ready(function(){
    $('#rzp-button2').click(function(e){
        e.preventDefault();
        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var pincode = $("[name='pincode']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();
        if(fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == ""  || pincode == "" ){
            swal("Alert!", "All fields are mandatory", "error");

            return false;
        }
        else{

            $.ajax({
                method : "GET",
                url: "/proceed-to-pay2",
                success: function(response){
                    // console.log(response);
                    var options = {
                        "key": "rzp_test_Ub6QFBei8ww2Pg", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Ecart", //your business name
                        "description": "Thankyou for buying",
                        "image": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/e-cart-design-template-0850ac300cfc66e069124f37ae291dea_screen.jpg?ts=1635403878",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the id obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data = {
                                'fname' : fname,
                                'lname' : lname,
                                'email' : email,
                                'phone' : phone,
                                'address' : address,
                                'city' : city,
                                'state' : state,
                                // 'country' : country,
                                'pincode' : pincode,
                                'payment_mode' : 'Razorpay',
                                'payment_id' : responseb.razorpay_payment_id,
                                csrfmiddlewaretoken : token
                            }
                            $.ajax({
                                method: 'POST',
                                url: '/placeorder2',
                                data: data,
                                success : function(responsec){
                                    swal("Congratulations",responsec.status,"success").then((value) => {
                                        window.location.href = '/myorder'
                                    })
                                }
                            })
                        },
                        "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                            "name": fname+' '+lname, //your customer's name
                            "email": email, 
                            "contact": phone  //Provide the customer's phone number for better conversion rates 
                        },
                        
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
            
                    rzp1.open();


                }
            })

    

        }

        
    })
});