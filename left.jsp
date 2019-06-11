<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2019/6/10 0010
  Time: 12:40
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<div class="M-left" style="width: 70%;height: 500px;background: bisque;float: left;">
    <% for( int i=0;i<25;i++){%>
    <img src="/pic_down/<%=i%>.jpg" alt="<%=i%>" style="width: 100px;height: 100px;">
    <%}%>

    <div>
        <a href="index.jsp">第一页</a>&nbsp;
        <a href="index2.jsp">第二页</a>
    </div>
</div>
