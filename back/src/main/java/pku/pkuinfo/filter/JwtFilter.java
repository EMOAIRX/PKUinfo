package pku.pkuinfo.filter;

import com.alibaba.fastjson.JSON;
import com.auth0.jwt.interfaces.Claim;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import pku.pkuinfo.utils.Result;
import pku.pkuinfo.utils.JwtUtils;

import java.io.IOException;
import java.util.Map;

/**
 * JWT过滤器
 */
@Slf4j
//@WebFilter(filterName = "JwtFilter", urlPatterns = "/api/admin/*")
@WebFilter(filterName = "JwtFilter", urlPatterns = "/*")
public class JwtFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        Filter.super.init(filterConfig);
        System.out.println("Filter established");
    }

    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException, ServletException {
        final HttpServletRequest request = (HttpServletRequest) req;
        final HttpServletResponse response = (HttpServletResponse) res;
        response.setCharacterEncoding("UTF-8");

        System.out.println("Request detected");

        // 放行预检请求
        if ("OPTIONS".equals(request.getMethod())) {
            response.setStatus(HttpServletResponse.SC_OK);
            chain.doFilter(request, response);
        } else {
            // 无Token
            if (request.getHeader("authorization") == null) {
                response.getWriter().write(JSON.toJSONString(Result.error("没有Token!")));
                return;
            }
            // 有Token
            final String token = request.getHeader("authorization").replace("Bearer ", "");

            Map<String, Claim> userData = JwtUtils.verifyToken(token);
            // 验证失败
            if (userData == null) {
                response.getWriter().write(JSON.toJSONString(Result.error("Token不合法!")));
                return;
            }
            // 验证成功放行
            chain.doFilter(req, res);
        }
    }

    @Override
    public void destroy() {
        Filter.super.destroy();
    }
}