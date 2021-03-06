$(document).ready(function() {
	var $myForm = $("#delete-entry")
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
        	$("#result").html('<div class="alert alert-dark"><button type="button" class="close">×</button>Entry deleted</div>');
        	window.setTimeout(function() {
                $(".alert").fadeTo(500, 0).slideUp(500, function(){
                    $(this).remove(); 
                });
            }, 5000);
          	$('.alert .close').on("click", function(e){
                $(this).parent().fadeTo(500, 0).slideUp(500);
             });
            $('.entries').load(document.URL + ' .entries');
        	$myForm[0].reset(); // reset form data
    }

    	function handleFormError(jqXHR, textStatus, errorThrown){
        	console.log(jqXHR)
        	console.log(textStatus)
        	console.log(errorThrown)
    }
	})
})

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})