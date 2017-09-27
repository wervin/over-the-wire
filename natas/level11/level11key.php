<?php 
	//RAPPEL :
	//Original_Data XOR KEY = Encrypted_Data
	//Original_Data XOR Encrypted_Data = KEY

	$orig_cookie = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw');  
	function xor_encrypt($in) {  
		$text = $in;  
		$key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
		print "$text\n";
		print "$key\n";
		$outText = '';  
		// Iterate through each character  
		for($i=0;$i<strlen($text);$i++) {  
			$outText .= $text[$i] ^ $key[$i % strlen($key)];  
		}		  
		return $outText;  
	}	  
	
	print xor_encrypt($orig_cookie);
 
?>  
