$(document).ready(function() {
	var $myForm = $("#userlist-entry-form")
	$myForm.submit(function(event) {
		event.preventDefault()
		var $formData = $(this).serialize()
		var $endpoint = $myForm.attr("data-url") || window.location.href
		$.ajax({
			method: "POST",
			url: $endpoint,
			data: $formData,
			success: handleFormSuccess,
			error: handleFormError,
		})
		function handleFormSuccess(data, textStatus, jqXHR){
        	console.log(data)
        	console.log(textStatus)
        	console.log(jqXHR)
        	alert("Added to list")
        	$myForm[0].reset(); // reset form data
    }

    	function handleFormError(jqXHR, textStatus, errorThrown){
        	console.log(jqXHR)
        	console.log(textStatus)
        	console.log(errorThrown)
        	alert("This book could not be added. Is it already in your list?")
    }
	})
})