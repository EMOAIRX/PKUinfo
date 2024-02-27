package pku.info.global;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import pku.info.secure.JWTInterceptor;

@Configuration
public class InterceptorRegister implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new JWTInterceptor())
                .addPathPatterns("/auth/**")
                .addPathPatterns("/admin/**")
                .excludePathPatterns("/admin/login");
    }
}
