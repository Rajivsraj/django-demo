function validation(){
    var en = document.forms["student_details"] ["Enrollment_Number"].value
    var n = document.forms["student_details"] ["First Name"].value
    var l = document.forms["student_details"] ["Last Name"].value
    var g = document.forms["student_details"] ["gender"].value
    var em = document.forms["student_details"] ["Email"].value
    var ph = document.forms["student_details"] ["Phone Number"].value
    var dob = document.forms["student_details"] ["dob"].value
    var Add = document.forms["student_details"] ["Address"].value
    var city = document.forms["student_details"] ["City"].value
    var state = document.forms["student_details"] ["State"].value
    var zip = document.forms["student_details"] ["Zip"].value
    var faname = document.forms["student_details"] ["fat"].value
    var faph = document.forms["student_details"] ["Fatp"].value
    var warnshow;
    var warning;
    var flag;

    if(en == ""){
        warning = document.getElementById("Enrollment")  // This is the input Field
        warnshow = document.getElementById("enwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Please put Enrollment No."
        warnshow.style.fontSize = "13px"
        flag = false
    }

    if(isNaN(en) == true){
        warning = document.getElementById("Enrollment")  // This is the input Field
        warnshow = document.getElementById("enwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Put Numbers Only."
        warnshow.style.fontSize = "13px"
        flag = false
    }

    
    if(n == ""){
        warning = document.getElementById("fname")  // This is the input Field
        warnshow = document.getElementById("fwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Please put First Name."
        warnshow.style.fontSize = "13px"
        flag = false
    }

    // if(l == ""){
    //     warning = document.getElementById("lname")  // This is the input Field
    //     warnshow = document.getElementById("lwarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Please put Last Name."
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }


    // if(g.value != "Male" || g.value != "Female" || g.value != "Others" ){
    //     warning = document.getElementById("gender")  // This is the input Field
    //     warnshow = document.getElementById("genwarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Please Select Gender."
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }


    if(em == ""){
        warning = document.getElementById("email")  // This is the input Field
        warnshow = document.getElementById("emwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Please put Email."
        warnshow.style.fontSize = "13px"
        flag = false
    }

    if(ph == ""){
        warning = document.getElementById("ph1")  // This is the input Field
        warnshow = document.getElementById("phwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Please put Phone No."
        warnshow.style.fontSize = "13px"
        flag = false
    }

    if(isNaN(ph) == true){
        warning = document.getElementById("ph1")  // This is the input Field
        warnshow = document.getElementById("phwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Put Valid Number."
        warnshow.style.fontSize = "13px"
        flag = false
    }

    if(dob == ""){
        warning = document.getElementById("dob")  // This is the input Field
        warnshow = document.getElementById("dbwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Please put Date of Birth"
        warnshow.style.fontSize = "13px"
        flag = false
    }

    if(Add == ""){
        warning = document.getElementById("address1")  // This is the input Field
        warnshow = document.getElementById("Addwarn")  // This is the span tag below input which shows the error
        warning.style.border="2px solid red"
        warning.placeholder="This Field is required"
        warnshow.style.display = "inline"
        warnshow.innerHTML = "Please put your Address"
        warnshow.style.fontSize = "13px"
        flag = false
    }

    // if(city == ""){
    //     warning = document.getElementById("city")  // This is the input Field
    //     warnshow = document.getElementById("cwarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Please Select a City"
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }

    // if(state == ""){
    //     warning = document.getElementById("state")  // This is the input Field
    //     warnshow = document.getElementById("swarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Please Select a State"
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }

    // if(zip == ""){
    //     warning = document.getElementById("zip")  // This is the input Field
    //     warnshow = document.getElementById("zwarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Please put your Area`s Zip"
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }

    // if(faname == ""){
    //     warning = document.getElementById("fathername")  // This is the input Field
    //     warnshow = document.getElementById("fawarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Put your Father`s Name"
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }

    // if(faph == ""){
    //     warning = document.getElementById("fph1")  // This is the input Field
    //     warnshow = document.getElementById("fapwarn")  // This is the span tag below input which shows the error
    //     warning.style.border="2px solid red"
    //     warning.placeholder="This Field is required"
    //     warnshow.style.display = "inline"
    //     warnshow.innerHTML = "Put your Father`s Phone No."
    //     warnshow.style.fontSize = "13px"
    //     flag = false
    // }




    if(flag == false){
       
        return false;

    }

    else{

        return true;

    }
}


function number_validation(){
    var en = document.forms["student_details"] ["Enrollment_Number"].value
    var n = document.forms["student_details"] ["First Name"].value
    var l = document.forms["student_details"] ["Last Name"].value
    var g = document.forms["student_details"] ["gender"].value
    var em = document.forms["student_details"] ["Email"].value
    var ph = document.forms["student_details"] ["Phone Number"].value
    var dob = document.forms["student_details"] ["dob"].value
    var Add = document.forms["student_details"] ["Address"].value
    var city = document.forms["student_details"] ["City"].value
    var state = document.forms["student_details"] ["State"].value
    var zip = document.forms["student_details"] ["Zip"].value
    var faname = document.forms["student_details"] ["fat"].value
    var faph = document.forms["student_details"] ["Fatp"].value
    var warnshow;
    var warning;
    var flag;


    if(en != ""){
        warning = document.getElementById("Enrollment")  // This is the input Field
        warnshow = document.getElementById("enwarn")  // This is the span tag below input which shows the error
        warning.style.border="1px solid skyblue"
        warnshow.style.display = "none"
    }

    
    if(n == ""){
        warning = document.getElementById("fname")  // This is the input Field
        warnshow = document.getElementById("fwarn")  // This is the span tag below input which shows the error
        warning.style.border="1px solid skyblue"
        warnshow.style.display = "none"
    }
  

    if(em == ""){
        warning = document.getElementById("email")  // This is the input Field
        warnshow = document.getElementById("emwarn")  // This is the span tag below input which shows the error
        warning.style.border="1px solid skyblue"
        warnshow.style.display = "none"
    }

    if(ph == ""){
        warning = document.getElementById("ph1")  // This is the input Field
        warnshow = document.getElementById("phwarn")  // This is the span tag below input which shows the error
        warning.style.border="1px solid skyblue"
        warnshow.style.display = "none"
    }

    if(dob == ""){
        warning = document.getElementById("dob")  // This is the input Field
        warnshow = document.getElementById("dbwarn")  // This is the span tag below input which shows the error
        warning.style.border="1px solid skyblue"
        warnshow.style.display = "none"
    }

    if(Add == ""){
        warning = document.getElementById("address1")  // This is the input Field
        warnshow = document.getElementById("Addwarn")  // This is the span tag below input which shows the error
        warning.style.border="1px solid skyblue"
        warnshow.style.display = "none"
    }
}
