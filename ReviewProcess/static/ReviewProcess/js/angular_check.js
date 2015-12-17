
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
                $('#sel_ques_'+$(this)[0].id).attr("name",'sel_ques_'+$(this)[0].id)
                 $('#sel_ques_'+$(this)[0].id).attr("value",$(this)[0].id);
                  i = i+1;

        			}
        			else{
        					currentProgress -= parseInt($(this)[0].value);
                  $('#sel_ques_'+$(this)[0].id).removeAttr("name");
                  $('#sel_ques_'+$(this)[0].id).removeAttr("value");
                  i = i-1;
        			}
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
             var values = new Array();
              $.each($("input[name='checkboxlist']:checked"), function() {
              values.push($(this)[0].id);
            });
            $('#selectcount').attr("value",values)
    	}
    	else{
    		$(":submit").attr("disabled", true)
    	}
 }
  $(":checkbox").click(adjustProgress);
  $('#userid').attr("value",$('select[name="selectbasic"] option:selected').val())


$('#selectbasic').change(function(){
        $('#userid').attr("value",$('select[name="selectbasic"] option:selected').val())
});

});

