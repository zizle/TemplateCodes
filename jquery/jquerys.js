//1. 生成唯一的UUID码
function generateUUID() {
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}

// 2.获取浏览器cookie, 参数为cookie名, 如: 'csrf_token'
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// 3.阻止表单的默认提交, ajax请求写在里面
$('.form').submit(function (e) {
    e.preventDefault()


}

// 4. 获取input标签内radio的内容
$('.类名[name=""]:checked').val()
$('.类名:radio:checked').val()

// 5.表单ajax写法
// html<script>导入jquery.form.min.js使用
// 首先要现在html的form标签中将需要的内容写上name属性，阻止表单的自动提交
$(function () {
    $(".release_form").submit(function (e) {
        e.preventDefault()
        $(this).ajaxSubmit({
            // 读取富文本编辑器里面的文本信息
            // 在提交之前，对参数进行处理
            beforeSubmit: function (request) {
                for (var i = 0; i < request.length; i++) {
                    var item = request[i];
                    if (item["name"] == "content") {
                        item["value"] = tinyMCE.activeEditor.getContent()
                    }
                }
            },
            url:'/user/release_news',
            type:'post',
            headers:{'X-CSRFToken': getCookie('csrf_token')},
            // 不能用.done()语法
            success:function (response) {
                if (response.errno=='0'){
                    alert(response.errmsg);
                    // 选中索引为6的左边单菜单
                    window.parent.fnChangeMenu(6);
                    // 滚动到顶部
                    window.parent.scrollTo(0, 0)
                }else{alert(response.errmsg)}
            }
        })
    })
});

// 6. 富文本插件的使用，结合tinymce文件夹和设置文件
//     <script src="tinymce/tinymce.min.js"></script>
//     <script src="tinymce_setup.js"></script>

//7. 分页插件，导入jquery.pagination.min.js使用
//  <script>
//     $(function(){
//         $("#pagination").pagination({
//             currentPage: 2,
//             totalPage: 3,
//             callback: function(current) {
//                 alert('分页');
//             }
//         });
//     });
//  </script>

// 8.二维图表工具(折线，柱状), html中嵌入如下标签，要导入echarts.min.js使用
// <script>
//     var oChart = echarts.init(document.getElementById('chart_show'));
//     var chartopt = {
//                 title:{
//                     text: '用户登录活跃数',
//                     left: 'center',
//                     top: '10'
//                 },
//                 tooltip:{
//                     trigger: 'axis'
//                 },
//                 legend: {
//                     data:['active'],
//                     top: '40'
//                 },
//                 toolbox: {
//                     show : true,
//                     feature : {
//                         mark : {show: true},
//                         dataView : {show: true, readOnly: false},
//                         magicType : {show: true, type: ['line','bar']},
//                         restore : {show: true},
//                         saveAsImage : {show: true}
//                     }
//                 },
//                 calculable : true,
//                 xAxis : [
//                     {
//                         name: '今天',
//                         type : 'category',
//                         boundaryGap : false,
//                         data : ["08:15","09:15","10:15","11:15","12:15","13:15","14:15","15:15","16:15","17:15","18:15","19:15"]
//                     }
//                 ],
//                 yAxis : [
//                     {
//                         name: '活跃用户数量',
//                         type : 'value'
//                     }
//                 ],
//                 series : [
//                     {
//                         name:'active',
//                         type:'line',
//                         smooth:true,
//                         itemStyle: {normal: {areaStyle: {type: 'default'}, color: '#f80'}, lineStyle: {color: '#f80'}},
//                         data:[14951,14861,7186,15861,14951,14861,7186,14951,14861,7186,15861,14951]
//                     }],
//                 areaStyle:{
//                         normal:{
//                             color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
//                                 offset: 0,
//                                 color: 'rgba(255,136,0,0.39)'
//                             }, {
//                                 offset: .34,
//                                 color: 'rgba(255,180,0,0.25)'
//                             },{
//                                 offset: 1,
//                                 color: 'rgba(255,222,0,0.00)'
//                             }])
//
//                         }
//                     }
//
//                 };
//     oChart.setOption(chartopt);
// </script>

// 9.解析url中的查询字符串
// 获取: var query = decodeQuery(); user_id = query["user_id"]
function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}


