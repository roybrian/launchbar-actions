FasdUAS 1.101.10   ��   ��    k             l     ��  ��    � } https://apple.stackexchange.com/questions/105361/terminal-commands-for-application-windows-and-show-desktop-in-mountain-lion     � 	 	 �   h t t p s : / / a p p l e . s t a c k e x c h a n g e . c o m / q u e s t i o n s / 1 0 5 3 6 1 / t e r m i n a l - c o m m a n d s - f o r - a p p l i c a t i o n - w i n d o w s - a n d - s h o w - d e s k t o p - i n - m o u n t a i n - l i o n   
  
 l     ��������  ��  ��        l    
 ����  O    
    I   	�� ��
�� .HmSpEXECnull���     ****  m       �  � 
 l o c a l   k e y 1   =   n i l 
 l o c a l   k e y 2   =   n i l 
 l o c a l   f u n c t i o n   s h o w D e s k t o p ( ) 
     o s . e x e c u t e ( [ [ ' / S y s t e m / A p p l i c a t i o n s / M i s s i o n   C o n t r o l . a p p / C o n t e n t s / M a c O S / M i s s i o n   C o n t r o l '   1 ] ] ) 
     i f   k e y 1   t h e n 
         k e y 1 : d e l e t e ( ) 
     e n d 
   i f   k e y 2   t h e n 
       k e y 2 : d e l e t e ( ) 
   e n d 
 e n d 
 s h o w D e s k t o p ( ) 
 k e y 1   =   h s . h o t k e y . b i n d ( { } ,   ' e s c a p e ' ,   f u n c t i o n ( )   s h o w D e s k t o p ( )   e n d ) 
 k e y 2   =   h s . h o t k e y . b i n d ( { } ,   ' r e t u r n ' ,   f u n c t i o n ( )   s h o w D e s k t o p ( )   e n d ) 
��    m       �                                                                                      @ alis    6  Macintosh HD                   BD ����Hammerspoon.app                                                ����            ����  
 cu             Applications  /:Applications:Hammerspoon.app/      H a m m e r s p o o n . a p p    M a c i n t o s h   H D  Applications/Hammerspoon.app  / ��  ��  ��        l     ��������  ��  ��        l     ��  ��    &  tell application "System Events"     �   @ t e l l   a p p l i c a t i o n   " S y s t e m   E v e n t s "      l     ��  ��    @ :	tell (application process 1 whose frontmost of it = true)     �     t 	 t e l l   ( a p p l i c a t i o n   p r o c e s s   1   w h o s e   f r o n t m o s t   o f   i t   =   t r u e )   ! " ! l     �� # $��   # P J		click menu item "Hide Others" of menu 1 of menu bar item 2 of menu bar 1    $ � % % � 	 	 c l i c k   m e n u   i t e m   " H i d e   O t h e r s "   o f   m e n u   1   o f   m e n u   b a r   i t e m   2   o f   m e n u   b a r   1 "  & ' & l     �� ( )��   ( &  		set allWindows to every window    ) � * * @ 	 	 s e t   a l l W i n d o w s   t o   e v e r y   w i n d o w '  + , + l     �� - .��   - 0 *		repeat with i from 1 to count allWindows    . � / / T 	 	 r e p e a t   w i t h   i   f r o m   1   t o   c o u n t   a l l W i n d o w s ,  0 1 0 l     �� 2 3��   2  			tell window i    3 � 4 4   	 	 	 t e l l   w i n d o w   i 1  5 6 5 l     �� 7 8��   7 6 0				set value of attribute "AXMinimized" to true    8 � 9 9 ` 	 	 	 	 s e t   v a l u e   o f   a t t r i b u t e   " A X M i n i m i z e d "   t o   t r u e 6  : ; : l     �� < =��   <  			end tell    = � > >  	 	 	 e n d   t e l l ;  ? @ ? l     �� A B��   A  		end repeat    B � C C  	 	 e n d   r e p e a t @  D E D l     �� F G��   F  		end tell    G � H H  	 e n d   t e l l E  I J I l     �� K L��   K  end tell    L � M M  e n d   t e l l J  N�� N l     ��������  ��  ��  ��       �� O P��   O ��
�� .aevtoappnull  �   � **** P �� Q���� R S��
�� .aevtoappnull  �   � **** Q k     
 T T  ����  ��  ��   R   S   ��
�� .HmSpEXECnull���     ****�� � �j U ascr  ��ޭ