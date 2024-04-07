package com.example.sportapp.data.di

import dagger.Module;
import dagger.Provides;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import javax.inject.Singleton;

@Module
public class AppModule {

//    @Provides
//    @Singleton
    /*public ApiService provideApiService() {
        return new Retrofit.Builder()
            .baseUrl("http://200.151.12.44/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService.class);
        }
    }*/
}