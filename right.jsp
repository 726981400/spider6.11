<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2019/6/10 0010
  Time: 12:39
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<div class="M-right" style="width: 30%;height: 500px;background: red;float: right">
    <input type="file" name="" id="" multiple><br/>
    <img src="" alt="" class="img0" style="width:100px;height:100px;">
    <script>
        var file = document.querySelector("input");
        var img = document.querySelector("img.img0");

        file.onchange = function (ev) {
            console.log(this.files);
            var reader = new FileReader();
            reader.readAsDataURL(this.files[0]);
            reader.onload = function (ev1) {
                img.src = this.result;
            }
        }
    </script>
</div>

