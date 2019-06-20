//USER INTERFACE(FRONT-END)
$(document).ready(function(){
    $("form#qboxes").submit(function(event){
      event.preventDefault();
      var Q1 = parseInt($("input:radio[name=Question1]:checked").val());
      var Q2 = parseInt($("input:radio[name=Question2]:checked").val());
      var Q3 = parseInt($("input:radio[name=Question3]:checked").val());
      var Q4 = parseInt($("input:radio[name=Question4]:checked").val());
      var Q5 = parseInt($("input:radio[name=Question5]:checked").val());
      var Q6 = parseInt($("input:radio[name=Question6]:checked").val());
      var Q7 = parseInt($("input:radio[name=Question7]:checked").val());
      var Q8 = parseInt($("input:radio[name=Question8]:checked").val());
      var Q9 = parseInt($("input:radio[name=Question9]:checked").val());
      var Q10 = parseInt($("input:radio[name=Question10]:checked").val());
      var Q11 = parseInt($("input:radio[name=Question11]:checked").val());
      var Q12 = parseInt($("input:radio[name=Question12]:checked").val());
      var Q13 = parseInt($("input:radio[name=Question13]:checked").val());
      var Q14 = parseInt($("input:radio[name=Question14]:checked").val());
      var Q15 = parseInt($("input:radio[name=Question15]:checked").val());
      var Q16 = parseInt($("input:radio[name=Question16]:checked").val());
      var Q17 = parseInt($("input:radio[name=Question17]:checked").val());
      var Q18 = parseInt($("input:radio[name=Question18]:checked").val());

     
      var total = calculateScore(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16,Q17,Q18);
    //   var name=$("input#studentsname").val();
      $("#marks").text ("Hello, "+" your risk level is at "+ total + "%");
      grades(total);
    });
    $("#reload").click(function(){
      $("#marks").empty();
      $("#comment").empty();
      $("#reload").hide();
    });
    $("form#stest").submit(function(event){
          event.preventDefault();
          $("#qboxes").slideDown();
    });
  });
  //BUSINESS LOGIC(BACKEND)
    function calculateScore (ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15, ans16, ans17, ans18) {
      return (ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8+ans9+ans10+ans11+ans12+ans13+ans14+ans15+ans16+ans17+ans18)/18*100;
      };
  
    function grades(test) {
      if (test >= 80) {
        $("#comment").text ("Excellent Performance!Congratulations!");
        $("#reload").hide();
      } else if (test <= 50){
        $("#comment").text ("Oh no! You have performed poorly, please retake the test!");
        $("#reload").show();
      } else {
        $("#comment").text ("Fair performance!");
        $("#reload").hide();
      }
    };
  