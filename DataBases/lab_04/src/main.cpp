#include <cstdlib>
#include <cstdio>
#include <string>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    FILE *log;
    FILE *out;
    FILE *err;
    FILE *exc;
    log = fopen("sys.log", "w");
    out = fopen("out.log", "w");
    err = fopen("err.log", "w");
    exc = fopen("exc.log", "w");

    // no path to script
    if (argc < 2)
    {
        fprintf(log, "ERROR: app name not given\n");
        printf("ERROR: app name not given\n");
        exit(1);
    }

    // concatenate all arguments to 'path-string'
    // ./ + app_name + [args]
    std::string temp = "./";
    for (unsigned int i = 0; i < argc - 1; ++i)
        temp += std::string(argv[i + 1]) + " ";
    // remove extra space from end
    temp.erase(temp.length() - 1);
    const char *path = temp.c_str();

    // separate pipes for stdout and stderr
    int out_pipe[2], err_pipe[2];
    if (pipe(out_pipe) < 0 || pipe(err_pipe) < 0)
    {
        fprintf(log, "ERROR: FD\n");
        printf("ERROR: FD\n");
        exit(1);
    }

    // fork the process
    int STATUS;
    pid_t pid = fork();
    // child
    if (pid == 0)
    {
        close(out_pipe[0]);
        close(err_pipe[0]);
        dup2(out_pipe[1], 1);
        dup2(err_pipe[1], 2);
        close(out_pipe[1]);
        close(err_pipe[1]);

        // run the script
        STATUS = system(path);
        return WEXITSTATUS(STATUS);
    }
    // parent
    else
    {
        waitpid(pid, &STATUS, 0);
    }
    STATUS = WEXITSTATUS(STATUS);
    close(out_pipe[1]);
    close(err_pipe[1]);

    // read collected data
    char buff_out[1024], buff_err[1024];
    buff_out[read(out_pipe[0], buff_out, sizeof(buff_out))] = '\0';
    buff_err[read(err_pipe[0], buff_err, sizeof(buff_err))] = '\0';

    // print received stdout
    fprintf(out, "%s", buff_out);
    printf("%s", buff_out);
    // print received stderr
    fprintf(err, "%s", buff_err);
    printf("%s", buff_err);
    // print received exit code
    fprintf(exc, "exit code: %d\n", STATUS);
    printf("exit code: %d\n", STATUS);

    // close files
    fclose(log);
    fclose(out);
    fclose(err);
    fclose(exc);

    exit(0);
}