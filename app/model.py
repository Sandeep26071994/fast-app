from email.policy import default
from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id:int=Field(default=None)
    title:str=Field(default=None)
    content:str=Field(default=None)
    class Config:
        schema_extra={
            "post_demo":{
                "title":"some title about products",
                "content":"some content about products"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "name":"sandeep",
                "email":"sandeepvinay.k@reward360.co",
                "password":"Vicky@1994"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr=Field(default=None)
    password:str = Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "email":"sandeepvinay.k@reward360.co",
                "password":"Vicky@1994"
            }
        }