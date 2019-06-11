<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2019/6/9 0009
  Time: 1:40
  To change this template use File | Settings | File Templates.
--%>
<%--简约互动，简单的快乐--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>RainBow</title>
  </head>
  <body>
    <div class="top" style="width: 100%;height: 200px;background: blue" >
      头部
    </div>
    <div class="middle" style="width: 100%;height: 550px;background: blueviolet">
      <jsp:include page="left.jsp"/>
      <jsp:include page="right.jsp"/>
    </div>

  </body>
</html>
