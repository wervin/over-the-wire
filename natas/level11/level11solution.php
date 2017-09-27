<?php 
	//RAPPEL :
	//Original_Data XOR KEY = Encrypted_Data
	//Original_Data XOR Encrypted_Data = KEY

	function xor_encrypt() {  
		$text = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));  
		$key = "qw8J";  
		print "$text\n";
		print "$key\n";
		$outText = '';  
		// Iterate through each character  
		for($i=0;$i<strlen($text);$i++) {  
			$outText .= $text[$i] ^ $key[$i % strlen($key)];  
		}		  
		return $outText;  
	}	  
	
	print base64_encode(xor_encrypt());
 
?>  
