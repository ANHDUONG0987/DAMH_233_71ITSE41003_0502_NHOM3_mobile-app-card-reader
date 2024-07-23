<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible"
		content="IE=edge">
	<meta name="viewport"
		content="width=device-width, 
				initial-scale=1.0">
	<style>
		* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	}
	body {
	background-color: rgb(253, 254, 255);
	display: flex;
	justify-content: center;
	align-items: center;
}
.full {
	width: 50%;
	max-width: 1000px;
	min-height: 100px;
	background-color: rgb(245, 239, 231);
	margin: 0px;
	display: grid;
	grid-template-columns: 2fr 4fr;
}
.left {
	position: initial;
	background-color: rgb(126, 219, 231);
	padding: 20px;

}
.right {
	position: initial;
	background-color: rgb(162, 202, 206);
	padding: 20px;

}
.image, .Contact, .Skills, .Language, .Hobbies, .title, 
.Summary, .Experience, .Education, .project {
	margin-bottom: 30px;
}
.h2 {
	background-color: rgb(4, 96, 150);
}
	</style>
</head>

<body>
	<div class="full">
		<div class="left">
			<div class="image">
				<iframe src="https://assets.pinterest.com/ext/embed.html?id=694187730093268770" height="445" width="345" frameborder="0" scrolling="no" 
                alt="gfg-logo"
					style="width:100px;
							height:100px;">>
                </iframe>
					
			</div>
			<div class="Contact">
				<h2>Liên hệ</h2>
				<p>
					<b>Email id:</b>hien.2274802010239@vanlanguni.vn
				</p>
				<p>
					<b>Mobile no :</b>0844xxxxxx
				</p>
			</div>
			<div class="Skills">
				<h2>kĩ năng</h2>
				<ul>
					<li>
						<b>Programming Languages :
							Python</b>
					</li>
					<li>
						<b>Frontend : HTML5, CSS3,
							JavaScript</b>
					</li>
					
				</ul>
			</div>
			<div class="Language">
				<h2>Ngôn ngữ</h2>
				<ul>
					<li>Tiếng anh</li>
					<li>Tiếng việt</li>
				</ul>
			</div>
			
		</div>
		<div class="right">
			<div class="name">
				<h1>THÀNH VIÊN</h1>
			</div>
			<div class="title">
				<p>Quản lý dự án xây dựng ứng dụng mobile app</p>
			</div>
			<div class="Summary">
				<h2>Giới thiệu</h2>
				<p>
					Tôi là một thành viên trong team phát triển dự án<br>
                    XÂY DỰNG MỘT ỨNG DỤNG APP MOBILE ĐỌC CÁC THÔNG TIN CỦA THẺ VISA MASTER CÓ GẮN CHIP
				</p>
			</div>
			<div class="Experience">
				<h2>Kinh nghiệm</h2>
				<li>xây dựng trang chủ login của app mobile</li>
			
				
				
			</div>
			<div class="Education">
				<h2>Học vấn</h2>
				<table>
					<tr>
						<th>University/college </th>
						<th>Passing year </th>
					</tr>
					<tr>
						<td>Văn lang university</td>
						<td>2022_2026</td>
					</tr>
				</table>
			</div>
			<div class="project">
				<ul>
					<li>
						<h2>Dự án 1</h2>
						<p>
							XÂY DỰNG MỘT ỨNG DỤNG APP MOBILE ĐỌC CÁC THÔNG TIN CỦA THẺ VISA MASTER CÓ GẮN CHIP
						</p>
					</li>
					
				</ul>
			</div>
		</div>
	</div>
</body>

</html>
