$(document).ready(function(){
	$('#somebuttonid').click(function(){
        var tbarray = new Array();
        $('.tb_circ').each(function(){
        	tbarray.push($(this).val()); //You will have a array tbarray with all the values of textboxes
        });
        $('#somehiddenelementid').val(tbarray);
        $('#somehiddenelementidcontainingform').submit(); //Make sure your action is set,you can access like $_post['$somehiddenelmentname'];
    });
});