jQuery.validator.setDefaults({
		  	debug: true,
		  	success:  function(label){
        		label.attr('id', 'valid');
   		 	},
		});
$( "#myform" ).validate({
		  	rules: {
			    password: "required",
		    	comfirm_password: {
		      		equalTo: "#password"
		    	}
		  	},
		  	messages: {
		  		uname: {
		  			required: "Please enter a username"
		  		},
				name: {
					required: "Please enter a name"
				},
		  		dob: {
		  			required: "Please enter a lastname"
		  		},
		  		address: {
		  			required: "Please provide an email"
		  		},
				phone: {
					required: "Please enter phone number"
				},
		  		password: {
	  				required: "Please enter a password"
		  		},
		  		comfirm_password: {
		  			required: "Please enter a password",
		      		equalTo: "Wrong Password"
		    	}
		  	}
		});