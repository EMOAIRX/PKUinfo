package pku.pkuinfo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@ServletComponentScan(basePackages = "pku.pkuinfo.filter")
@EnableCaching
public class PkUinfoApplication {

    public static void main(String[] args) {
        SpringApplication.run(PkUinfoApplication.class, args);
    }

}
