function get_mobile_code_function(){

			var mobile_num=$("#mobile_number").val();
			alert(mobile_num)


			$.ajax({
				//必须要写的四个参数,顺序不限
                url:"/api/get_mobile_code/",
                //处理页面的路径
                data:{mobile:mobile_num},
                //传递的数据.提交数一般以json格式来写,key是自定义的,:后面的值 就是上面的值
                type:"POST",
                //数据的提交传递方式,GET,POST 最好用POST
                datatype:"JSON",
                //返回值的类型,TEXT,JSON,XML三种类型可选
                success:function(data){
                //如果ajax执行成功,返回来调用success函数即回调函数,返回值以参数的形式返回

                    alert(data);

                },

		});
		}

function registerBymobile(){

			var code=$("#mobile_number").val();
			alert(mobile_num)


			$.ajax({
				//必须要写的四个参数,顺序不限
                url:"/api/User_RegisterBymoblie/",
                //处理页面的路径
                data:{mobile:mobile_num},
                //传递的数据.提交数一般以json格式来写,key是自定义的,:后面的值 就是上面的值
                type:"POST",
                //数据的提交传递方式,GET,POST 最好用POST
                datatype:"JSON",
                //返回值的类型,TEXT,JSON,XML三种类型可选
                success:function(data){
                //如果ajax执行成功,返回来调用success函数即回调函数,返回值以参数的形式返回

                    alert(data);

                },

		});
		}

