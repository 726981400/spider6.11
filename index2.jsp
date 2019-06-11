<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2019/6/10 0010
  Time: 13:12
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
    <div class="M-left" style="width: 70%;height: 500px;background: bisque;float: left;">
        <% for( int i=25;i<50;i++){%>
        <img src="/pic_down/<%=i%>.jpg" alt="<%=i%>" style="width: 100px;height: 100px;">
        <%}%>

        <div>
            <a href="index.jsp">第一页</a>&nbsp;
            <a href="index2.jsp">第二页</a>
        </div>
    </div>
    <jsp:include page="right.jsp"/>
</div>
爬虫首页

</body>
</html>
