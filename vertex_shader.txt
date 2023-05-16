varying vec3 vN;
varying vec3 v;
varying vec4 color;
void main(void)  
{     
   v = vec3(gl_ModelViewMatrix * gl_Vertex);       
   vN = normalize(gl_NormalMatrix * gl_Normal);
   color = gl_Color;
   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;  
}