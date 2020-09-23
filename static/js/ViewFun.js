var editor = ace.edit("editor");
    editor.setTheme("ace/theme/nord_dark");
    document.getElementById('editor').style.fontSize='16px';
    editor.getSession().setMode("ace/mode/c_cpp");
    editor.setValue("#include <stdio.h>\nint main(){\n\n    return 0;\n}");
    editor.gotoLine(3);

    $("#output_show").hide();
    $("#compile_show").hide();
    $("#Test").hide();
    $("#compiling").hide();
    var extension;
    $("#languages").change(function () {
        var l =($(this).val());
        if (l=="PYTHON3"){
            editor.getSession().setMode("ace/mode/python");
            editor.setValue("print('Hello Python!!!')\n");
            editor.gotoLine(2);
            extension = '.py';
        }
        else if (l=="CPP14"){
        	editor.getSession().setMode("ace/mode/c_cpp");
            editor.setValue("#include <iostream>\nusing namespace std;\nint main(){\n\n    return 0;\n}\n");
            editor.gotoLine(4);
            extension = '.cpp';
        }
        else if (l=="C"){
        	editor.getSession().setMode("ace/mode/c_cpp");
            editor.setValue("#include <stdio.h>\nint main(){\n\n    return 0;\n}\n");
            editor.gotoLine(3);
            extension = '.c';
        }
        else if (l=="JAVA8"){
        	editor.getSession().setMode("ace/mode/java");
            editor.setValue("public class Java{\n    public static void main(String args[]){\n\n    }\n}\n");
            editor.gotoLine(3);
            extension = '.java';
        }
    });

    $('#customCheck1').click(function(){

    if ($("#customCheck1").prop("checked")){
        $("#Test").show();
    }
    else{
        $("#Test").hide();
    }

    });


	$(document).on('submit', '#post-code', function(e){
		e.preventDefault();
        $("#btn").prop('disabled', true);
        $("#compiling").show();
        $("#compiling_p").text("Compiling Code...");
		$.ajax({
			type: 'POST',
			url: 'result',
			data: {
				source: editor.getValue(),
				lang: $("#languages").val(),
				testcases: $("#Test").val(),
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function (json) {
			    $("#compiling").hide();
			    $("#btn").prop('disabled', false);
				$("#output_show").show();
				$("#compile_show").show();
				$("#TextArea_out").html(json.output);
				$("#TextArea_com").html(json.compile_status);
			},
			error: function(xhr){
			    $("#compiling").hide();
				$("#output_show").hide();
				$("#compile_show").hide();
			    alert(xhr);
			    $("#btn").prop('disabled', false);
			}
		});
	});

