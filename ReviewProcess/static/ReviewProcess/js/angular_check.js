
$(document).ready(function() {
  
  // get box count
  var count = 0;
  var checked = 0;
  function countBoxes() { 
    count = $("input[type='checkbox']").length;
    console.log(count);
  }
  
  countBoxes();
  $(":checkbox").click(countBoxes);
  
  // count checks
  
  /*function countChecked() {
    checked = $("input:checked").length;
    
    var percentage = parseInt(((checked / count) * 100),10);
    $(".progressbar-bar").progressbar({
            value: percentage
        });
    $(".progressbar-label").text(percentage + "%");
  }*/
  var currentProgress =0,i=0;
   function adjustProgress( checkbox )
    {

    			
    				if($("input:checked")[0] != undefined && $(this).prop("checked")){
        				currentProgress += parseInt($(this)[0].value);
        			}
        			else{
        					currentProgress -= parseInt($(this)[0].value);
        			}
        		

        //$( ".progressbar-bar" ).progressbar("value" , currentProgress )
        if(currentProgress <= 100 ){
        	$(".progressbar-bar").progressbar({
            value: currentProgress
        	});
        	$(".progressbar-label").text(currentProgress + "%");
        }
        
        if ( currentProgress > 100 )
        {
            alert( "You have exceeded the maximum value of 100" );
            $(this)[0].checked = false
            currentProgress -= parseInt($(this)[0].value)
        }
        if ( currentProgress == 100 )
        {
     	   $(":submit").removeAttr("disabled")
    	}
    	else{
    		$(":submit").attr("disabled", true)
    	}
 }
  $(":checkbox").click(adjustProgress);
  
});