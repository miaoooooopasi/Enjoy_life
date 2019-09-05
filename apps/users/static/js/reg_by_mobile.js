function reg_by_mobile(){


			var gmcode=$("#gmcode").val();
			alert(gmcode);
			var mobile_num=$("#mobile_number").val();
			alert(mobile_num);
			var pwd=$("#pwd").val();
			alert(pwd);


			$.ajax({
				//必须要写的四个参数,顺序不限
                url:"/api/User_RegisterBymoblie/",
                //处理页面的路径
                data:{
                    code:gmcode,
                    username:mobile_num,
                    password:pwd,
                    mobile:mobile_num,
                },
                //传递的数据.提交数一般以json格式来写,key是自定义的,:后面的值 就是上面的值
                type:"POST",
                //数据的提交传递方式,GET,POST 最好用POST
                datatype:"JSON",
                //返回值的类型,TEXT,JSON,XML三种类型可选
                success:function(data){
                //如果ajax执行成功,返回来调用success函数即回调函数,返回值以参数的形式返回
					alert(321);
                    alert(data['id']);


                },

		});
		}

