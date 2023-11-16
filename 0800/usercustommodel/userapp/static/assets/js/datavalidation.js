

function validdata() {


    var rollno = document.forms["login"]["enroll_no"].value;
    var fname = document.forms["login"]["first_name"].value;
    var stu_email = document.forms["login"]["email"].value;
    var stu_ph1 = document.forms["login"]["ph_1"].value;
    var stu_dob = document.forms["login"]["dob"].value;
    var add1 = document.forms["login"]["add_1"].value;
    var aadhar = document.forms["login"]["aadhar_no"].value;
    var father_nm = document.forms["login"]["father_nm"].value;
    var mother_nm = document.forms["login"]["mother_nm"].value;
    var zipcode = document.forms["login"]["zip_code"].value;

    var add;

    if (rollno == "") {


        inputerr = document.getElementById("roll")
        inputerr.style.border = "1px solid red"
        bord_er = document.getElementById("one")
        bord_er.innerHTML = "Please Fill this Field"
        bord_er.style.color = "red"
        bord_er.style.display = "block"
        add = false;

    }

    else if (rollno != "") {


        inputerr = document.getElementById("roll")
        inputerr.style.border = "1px solid skyblue"
        bord_er = document.getElementById("one")
        bord_er.style.display = "none"



    }


    if (fname == "") {

        int_err = document.getElementById("fn")
        int_err.style.border = "1px solid red"
        bod_er = document.getElementById("two")
        bod_er.innerHTML = "Please Fill this Field"
        bod_er.style.color = "red"
        bod_er.style.display = "block"
        add = false;



    }

    else if (fname != "") {

        int_err = document.getElementById("fn")
        int_err.style.border = "1px solid skyblue"
        bod_er = document.getElementById("two")
        bod_er.style.display = "none"


    }

    if (stu_email == "") {

        intupt_em = document.getElementById("email")
        intupt_em.style.border = "1px solid red"
        bod_em = document.getElementById("three")
        bod_em.innerHTML = "Please Fill this Field"
        bod_em.style.color = "red"
        bod_em.style.display = "block"
        add = false;


    }
    else if (stu_email != "") {

        intupt_em = document.getElementById("email")
        bod_em = document.getElementById("three")
        intupt_em.style.border = "1px solid skyblue"
        bod_em.style.display = "none"




    }

    if (stu_ph1.length < 10 || stu_ph1.length > 10) {


        int_ph = document.getElementById("phone")
        int_ph.style.border = "1px solid red"
        bod_ph = document.getElementById("one_4")
        bod_ph.innerHTML = "Please Fill this Field"
        bod_ph.style.color = "red"
        bod_ph.style.display = "block"
        add = false;

    }

    else if (stu_ph1 != "") {

        int_ph = document.getElementById("phone")
        bod_ph = document.getElementById("one_4")
        int_ph.style.border = "1px solid skyblue"
        bod_ph.style.display = "none"



    }

    if (stu_dob == "") {

        int_dob = document.getElementById("dob")
        int_dob.style.border = "1px solid red"
        bod_dob = document.getElementById("one_5")
        bod_dob.innerHTML = "Please Fill this Field"
        bod_dob.style.color = "red"
        bod_dob.style.display = "block"
        add = false;


    }

    else if (stu_dob != "") {

        int_dob = document.getElementById("dob")
        bod_dob = document.getElementById("one_5")
        int_dob.style.border = "1px solid skyblue"
        bod_dob.style.display = "none"


    }

    if (add1 == "") {

        int_add = document.getElementById("add1")
        int_add.style.border = "1px solid red"
        bod_add = document.getElementById("one_6")
        bod_add.innerHTML = "Please Fill this Field"
        bod_add.style.color = "red"
        bod_add.style.display = "block"
        add = false;

    }

    else if (add1 != "") {

        int_add = document.getElementById("add1")
        int_add.style.border = "1px solid skyblue"
        bod_add = document.getElementById("one_6")
        bod_add.style.display = "none"


    }




    if (aadhar.length < 12 || aadhar.length > 12) {

        int_adhar = document.getElementById("adhar")
        int_adhar.style.border = "1px solid red"
        bod_adhar = document.getElementById("one_9")
        bod_adhar.innerHTML = "Please Fill this Field"
        bod_adhar.style.color = "red"
        bod_adhar.style.display = "block"
        add = false;

    }

    else if (aadhar != "") {


        int_pic = document.getElementById("adhar")
        int_pic.style.border = "1px solid skyblue"
        bod_pic = document.getElementById("one_9")
        bod_pic.style.display = "none"

    }



    if (father_nm == "") {

        int_fn = document.getElementById("fathernm")
        int_fn.style.border = "1px solid red"
        bod_fn = document.getElementById("one_11")
        bod_fn.innerHTML = "Please Fill this Field"
        bod_fn.style.color = "red"
        bod_fn.style.display = "block"
        add = false;


    }

    else if (father_nm != "") {

        int_fn = document.getElementById("fathernm")
        int_fn.style.border = "1px solid skyblue"
        bod_fn = document.getElementById("one_11")
        bod_fn.style.display = "none"


    }

    if (mother_nm == "") {

        int_mn = document.getElementById("mothernm")
        int_mn.style.border = "1px solid red"
        bod_mn = document.getElementById("one_12")
        bod_mn.innerHTML = "Please Fill this Field"
        bod_mn.style.color = "red"
        bod_mn.style.display = "block"
        add = false;



    }

    else if (mother_nm != "") {

        int_mn = document.getElementById("mothernm")
        int_mn.style.border = "1px solid skyblue"
        bod_mn = document.getElementById("one_12")
        bod_mn.style.display = "none"



    }


    if (add == false) {
        alert("Please Fill All Fields")

        return false;
    }



}



function ErrorValidate() {
    msg = document.getElementById("errorcontainer")
    msg.style.display = "inline-block"

}


// =======================================================================================================================
// Login From Validation
// =======================================================================================================================

function login_validate() {


    var email = document.forms["login_form"]["email"].value;
    var password = document.forms["login_form"]["password"].value;
    var add2;


    if (email == "") {


        int_email = document.getElementById("em")
        int_email.style.border = "1px solid red"
        bord_em = document.getElementById("one")
        bord_em.innerHTML = "Please Fill this Field"
        bord_em.style.color = "red"
        bord_em.style.display = "block"
        add2 = false;

    }

    else if (email != "") {


        int_email = document.getElementById("em")
        int_email.style.border = "1px solid skyblue"
        bord_em = document.getElementById("one")
        bord_em.style.display = "none"



    }

    if (password == "") {


        int_pass = document.getElementById("pss")
        int_pass.style.border = "1px solid red"
        bord_pass = document.getElementById("two")
        bord_pass.innerHTML = "Please Fill this Field"
        bord_pass.style.color = "red"
        bord_pass.style.display = "block"
        add2 = false;

    }

    else if (password != "") {




        int_pass = document.getElementById("pss")
        int_pass.style.border = "1px solid skyblue"
        bord_pass = document.getElementById("two")
        bord_pass.style.display = "none"



    }


    if (add2 == false) {
        alert("Please Fill All Fields")

        return false;
    }


}

// =======================================================================================================================
// Register form validation 
// =======================================================================================================================

function register_validate() {
    var fullname = document.forms["register"]["name"].value;
    var email = document.forms["register"]["email"].value;
    var password = document.forms["register"]["password"].value;
    var repassword = document.forms["register"]["repassword"].value;
    var checkbox_value = document.getElementById("agreeTerms").checked;
    var status;

    if (fullname == "") {
        input_err_border = document.getElementById("name")
        input_err_border.style.border = "1px solid red"
        fullname_error = document.getElementById("one")
        fullname_error.style.display = "block"
        fullname_error.innerHTML = "Please Fill This Field"
        fullname_error.style.color = "red"
        status = false;
    }

    else if (fullname != "") {
        input_err_border = document.getElementById("name")
        input_err_border.style.border = "1px solid green"
        fullname_error = document.getElementById("one")
        fullname_error.innerHTML = ""
        fullname_error.style.display = "none"
    }

    if (email == "") {
        input_err_border = document.getElementById("email")
        input_err_border.style.border = "1px solid red"
        email_error = document.getElementById("two")
        email_error.innerHTML = "Please Fill This Field"
        email_error.style.color = "red"
        status = false;
    }

    else if (email != "") {
        input_err_border = document.getElementById("email")
        input_err_border.style.border = "1px solid green"
        email_error = document.getElementById("two")
        email_error.innerHTML = ""
        email_error.style.display = "none"
    }

    if (password == "") {
        input_err_border = document.getElementById("password")
        input_err_border.style.border = "1px solid red"
        password_error = document.getElementById("three")
        password_error.innerHTML = "Please Fill This Field"
        password_error.style.color = "red"
        status = false;
    }

    else if (password != "") {
        input_err_border = document.getElementById("password")
        input_err_border.style.border = "1px solid green"
        password_error = document.getElementById("three")
        password_error.innerHTML = ""
        password_error.style.color = "red"

    }

    if (repassword == "") {
        input_err_border = document.getElementById("repassword")
        input_err_border.style.border = "1px solid red"
        repassword_error = document.getElementById("four")
        repassword_error.innerHTML = "Please Fill This Field"
        repassword_error.style.color = "red"
        status = false;
    }

    else if (repassword != password) {
        input_err_border = document.getElementById("repassword")
        input_err_border.style.border = "1px solid red"
        repassword_error = document.getElementById("four")
        repassword_error.innerHTML = "Both Passwords Dosen`t Matches"
        repassword_error.style.display = "block"
        status = false;
    }


    else if (repassword == password) {
        input_err_border = document.getElementById("repassword")
        input_err_border.style.border = "1px solid green"
        repassword_error = document.getElementById("four")
        repassword_error.innerHTML = ""
        repassword_error.style.display = "none"
    }

    if (status == false) {
        alert("Please Fill All Fields")

        return false;
    }

    if (checkbox_value != true){
        checkbox_alert = document.getElementById("five")
        checkbox_alert.style.color = "red"
        checkbox_alert.style.fontWeight = "bold"
        checkbox_alert.innerHTML = "Please Agree to The Terms & Conditions."
        alert("Please Checkbox")
        return false;
    }

    else {
        checkbox_alert = document.getElementById("five")
        checkbox_alert.style.border = ""
        checkbox_alert.innerHTML = ""

        
    }





}



function password_pattern(){
    input_err_border = document.getElementById("password")
    input_err_border.title = "Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
    if (input_err_border.pattern) {
        input_err_border = document.getElementById("password")
        input_err_border.style.border = "1px solid red"
        password_error = document.getElementById("three")
        password_error.innerHTML = "Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
        password_error.style.color = "grey"
    }
       


}


// =============================================================================================================================
// Register form checkbox validation to check one box at a time

function register_checkbox_val(){
    parent_checkbox = document.forms["register"]["is_parent"].checked;
    faculty_checkbox = document.forms["register"]["is_faculty"].checked;


    print("hjdsfgyjxskjhfgdkusisuhhdhfdhfiusdf")

    if(parent_checkbox == true){
        faculty_checkbox.checked = false
    }

    if(faculty_checkbox == true){
        parent_checkbox = document.forms["register"]["is_parent"].checked;
        parent_checkbox.checked = false
    }
}





// function ErrorValid(){
//     msg2 = document.getElementById("error")
//     msg2.style.display = "inline-block"

// }