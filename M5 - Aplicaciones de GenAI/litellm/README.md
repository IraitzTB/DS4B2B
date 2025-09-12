# LiteLLM

[LiteLLM](https://www.litellm.ai/) es una solución de gateway que nos permite hacer una gestión eficiente de los recursos, con políticas de fall-back, limitación de presupuestos y permisos.

Seguid las instrucciones en https://docs.litellm.ai/#step-1-create-configyaml

Primero deberemos crear un fichero `litellm_config.yml' con la configuración necesaria:
```yaml
model_list:
  - model_name: gpt-5-mini
  ....
```
para luego poder instanciar `docker compose up`.

Con esto deberíamos poder llamar a nuestro endpoint particular:
```
import openai # openai v1.0.0+
client = openai.OpenAI(api_key="anything",base_url="http://0.0.0.0:4000") # set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])

print(response)
```