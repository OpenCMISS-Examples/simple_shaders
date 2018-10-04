varying vec2 vUv;
varying vec3 lightPos, eyeVertex, eyeNormal;
varying vec4 diffuse;
varying float qAttenuation, cAttenuation, lAttenuation;

void main()
{
    vUv = gl_Vertex.xy;
    gl_TexCoord[0] = gl_MultiTexCoord0;
    eyeVertex = vec3(gl_ModelViewMatrix * gl_Vertex);
    lightPos = gl_LightSource[0].position.xyz ;
    eyeNormal = vec3(gl_NormalMatrix * gl_Normal);
    diffuse = gl_Color;
    qAttenuation = gl_LightSource[0].quadraticAttenuation;
    cAttenuation = gl_LightSource[0].constantAttenuation;
    lAttenuation = gl_LightSource[0].linearAttenuation;
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
